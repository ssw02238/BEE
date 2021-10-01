#status & object
from django.core.checks import messages
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect, HttpResponse

#rest api
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

#model & serializing
from .models import Corporate, News
from .seiralizers import CorporateSerializer, CorporateDetailSerializer, NewsSerializer

#Authentication & Authorization
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances
from sqlalchemy import create_engine
import pymysql

# import time
# import schedule

#기업 디테일 모든 정보를 다 넣어놓음
@api_view(['GET'])
def corp_detail(request, corp_id):
    corp = get_object_or_404(Corporate, id=corp_id)
    corp_serializer = CorporateDetailSerializer(corp)
    return Response(corp_serializer.data)
    
@api_view(['GET'])
def corp_news(request, corp_id):
    news = get_list_or_404(News.objects.filter(corporate_id=corp_id))
    serializers = NewsSerializer(news, many=True)
    return Response(serializers.data)

#유사 기업
@api_view(['GET'])
def similar_corp(request, corp_id):
    corp = get_object_or_404(Corporate, id=corp_id)
    
    first = CorporateSerializer(get_object_or_404(Corporate, id=corp.first)).data
    second = CorporateSerializer(get_object_or_404(Corporate, id=corp.second)).data
    third = CorporateSerializer(get_object_or_404(Corporate, id=corp.third)).data

    sim_corps = {
        'corporates': [first, second, third]
    }

    return JsonResponse(sim_corps)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def add_scrap(request, corp_id):
    corp = get_object_or_404(Corporate, pk=corp_id)

    #스크랩 취소 (이미 스크랩한 유저)
    if corp.scrap_user.filter(pk=request.user.pk).exists():
        corp.scrap_user.remove(request.user)
        return Response({'messages': '스크랩 취소'}, status=status.HTTP_204_OK)

    #스크랩 추가
    else:
        corp.scrap_user.add(request.user)
        return Response({'messages': '스크랩 성공'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def search(request, corp_name):
    #404 띄울 것인지 고민하라
    corp = get_object_or_404(Corporate, name=corp_name)
    serializer = CorporateSerializer(corp)
    return Response(serializer.data)

@api_view(['GET'])
def similarity(request):
    # DB 불러와서 유사도 분석 후 temp 테이블에 결과 저장
    db_connection_str = 'mysql+pymysql://admin:1q2w3e4r5t!@bee.cjkrtt0iwcwz.ap-northeast-2.rds.amazonaws.com/BEE'
    db_connection = create_engine(db_connection_str)

    query = "SELECT * FROM corporates_corporate"
    df = pd.read_sql(query, db_connection)

    corp_rating = df[['E_rating', 'S_rating', 'G_rating']]
    sim = euclidean_distances(corp_rating, corp_rating)
    sim = pd.DataFrame(sim.argsort()[:,1:4], columns=['first', 'second', 'third'])
    sim_df = sim + 1

    df['first'] = sim_df['first']
    df['second'] = sim_df['second']
    df['third'] = sim_df['third']
    df.to_sql(name='temp', con=db_connection, if_exists='replace', index=False)

    # DB 연결해서 temp 테이블에 저장한 결과를 corporate 테이블로 옮기기
    db = pymysql.connect(
        user='admin',
        passwd='1q2w3e4r5t!',
        host='bee.cjkrtt0iwcwz.ap-northeast-2.rds.amazonaws.com',
        db='BEE',
        charset='utf8'
        )

    cursor = db.cursor()
    update_sql = """
        UPDATE corporates_corporate, temp
        SET corporates_corporate.first = temp.first, corporates_corporate.second = temp.second, corporates_corporate.third = temp.third
        WHERE corporates_corporate.id = temp.id;
        """

    cursor.execute(update_sql)
    db.commit()
    db.close()

    return Response(df)



# 매일 정해진 시간에 함수 실행
# schedule.every().day.at("00:00").do(similarity)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
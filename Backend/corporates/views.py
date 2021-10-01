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

    E_query = "SELECT total, news_pos_cnt, news_neg_cnt FROM corporates_environment"
    E_df = pd.read_sql(E_query, db_connection)

    S_query = "SELECT total, news_pos_cnt, news_neg_cnt FROM corporates_social"
    S_df = pd.read_sql(S_query, db_connection)

    G_query = "SELECT total, news_pos_cnt, news_neg_cnt FROM corporates_governance"
    G_df = pd.read_sql(G_query, db_connection)

    df['E_rating'] = (E_df['news_pos_cnt']+1)/(E_df['news_pos_cnt']+E_df['news_neg_cnt']+2)*20 + E_df['total']*0.8
    df['S_rating'] = (S_df['news_pos_cnt']+1)/(S_df['news_pos_cnt']+S_df['news_neg_cnt']+2)*20 + S_df['total']*0.8
    df['G_rating'] = (G_df['news_pos_cnt']+1)/(G_df['news_pos_cnt']+G_df['news_neg_cnt']+2)*20 + G_df['total']*0.8
    df['ESG_rating'] = df['E_rating'] + df['S_rating'] + df['G_rating']
    df = df.round(3)

    corp_rating = df[['E_rating', 'S_rating', 'G_rating']]
    sim = euclidean_distances(corp_rating, corp_rating)
    sim = pd.DataFrame(sim.argsort()[:,1:4], columns=['first', 'second', 'third'])
    sim_df = sim + 1

    df[['first', 'second', 'third']] = sim_df[['first', 'second', 'third']]
    df.to_sql(name='temp_corp', con=db_connection, if_exists='replace', index=False)

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
        UPDATE corporates_corporate, temp_corp
        SET
        corporates_corporate.E_rating = temp_corp.E_rating,
        corporates_corporate.S_rating = temp_corp.S_rating,
        corporates_corporate.G_rating = temp_corp.G_rating,
        corporates_corporate.ESG_rating = temp_corp.ESG_rating,
        corporates_corporate.first = temp_corp.first,
        corporates_corporate.second = temp_corp.second,
        corporates_corporate.third = temp_corp.third
        WHERE corporates_corporate.id = temp_corp.id;
        """

    cursor.execute(update_sql)
    db.commit()
    db.close()

    return Response(status=status.HTTP_200_OK)



# 매일 정해진 시간에 함수 실행
# schedule.every().day.at("00:00").do(similarity)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
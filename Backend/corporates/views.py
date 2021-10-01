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
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
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

#유사 기업 (기업간 기업)
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



    # mbti 결과 기반 추천 DB 업데이트
    mbti_query = "SELECT * FROM accounts_mbti"
    mbti_df = pd.read_sql(mbti_query, db_connection)
    user_mbti = mbti_df[['e_score', 's_score', 'g_score']]
    corp_df = df[['E_rating', 'S_rating', 'G_rating']]

    # 코사인 유사도가 높은 20개 기업 순서대로 출력
    cos_sim = cosine_similarity(user_mbti, corp_df)
    cos_sim_rank = cos_sim.argsort()[:,:-21:-1]

    # 각 사용자마다 코사인 유사도 상위 20개 기업에 대해 유클리디안 거리 비교 및 상위 3개 출력
    for i in range(len(cos_sim_rank)):
        rank = cos_sim_rank[i]
        cos_sim_corps = corp_df.iloc[rank]
    
        sim_dist = euclidean_distances(user_mbti.iloc[i:i+1], cos_sim_corps)
        dist_sim_rank = sim_dist.argsort()[0][:3]
        dist_sim_corps = cos_sim_corps.index[dist_sim_rank]
        mbti_df.loc[i,['first', 'second', 'third']] = dist_sim_corps

    mbti_df.to_sql(name='temp_mbti', con=db_connection, if_exists='replace', index=False)



    # DB 연결해서 temp 테이블에 저장한 결과를 원하는 테이블로 옮기기
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

    mbti_sql = """
        UPDATE accounts_mbti, temp_mbti
        SET
        accounts_mbti.first = temp_mbti.first,
        accounts_mbti.second = temp_mbti.second,
        accounts_mbti.third = temp_mbti.third
        WHERE accounts_mbti.id = temp_mbti.id;
        """

    cursor.execute(update_sql)
    cursor.execute(mbti_sql)
    db.commit()
    db.close()

    return Response(status=status.HTTP_200_OK)



# 매일 정해진 시간에 함수 실행
# schedule.every().day.at("00:00").do(similarity)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
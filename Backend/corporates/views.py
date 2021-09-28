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

from django.db import connection
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances
# from sqlalchemy import create_engine
# import pymysql

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
    corp = Corporate.objects.all().values()
    corp_df = pd.DataFrame(corp)

    corp_rating = corp_df[['E_rating', 'S_rating', 'G_rating']]

    sim = euclidean_distances(corp_rating, corp_rating)
    sim = pd.DataFrame(sim.argsort()[:,1:4], columns=['first', 'second', 'third'])
    sim_df = sim + 1

    corp_df['first'] = sim_df['first']
    corp_df['second'] = sim_df['second']
    corp_df['third'] = sim_df['third']

    # db_connection_str = 'mysql+pymysql://[db유저이름]:[db password]@[host address]/[db name]'
    # db_connection = create_engine(db_connection_str)

    # corp_df.to_sql(name='corporates_corporate', con=db_connection, flavor='mysql', if_exists='append', index=False)
    return Response(corp_df)
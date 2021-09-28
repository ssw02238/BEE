#status & object
from django.core.checks import messages
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect, HttpResponse

#rest api
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

#model & serializing
from corporates.models import Corporate, News
from corporates.seiralizers import CorporateSerializer, CorporateDetailSerializer, NewsSerializer

#Authentication & Authorization
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

#etc
from datetime import date, timedelta
from django.db.models import Count

#ESG 총점 랭킹 200개 출력 
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def esg_ranking(reqeust):
    corp_list = get_list_or_404(Corporate.objects.order_by('-ESG_rating'))
    serializer = CorporateSerializer(corp_list, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def e_ranking(reqeust):
    corp_list = get_list_or_404(Corporate.objects.order_by('-E_rating'))
    serializer = CorporateSerializer(corp_list, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def s_ranking(reqeust):
    corp_list = get_list_or_404(Corporate.objects.order_by('-S_rating'))
    serializer = CorporateSerializer(corp_list, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def g_ranking(reqeust):
    corp_list = get_list_or_404(Corporate.objects.order_by('-G_rating'))
    serializer = CorporateSerializer(corp_list, many=True)
    
    return Response(serializer.data)

#ESG 랭킹 1등
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def bestcorp(request):
    corp = get_object_or_404(Corporate.objects.order_by('-ESG_rating')[:1])
    serializer = CorporateDetailSerializer(corp)
    
    return Response(serializer.data)
    
#신문 기사에서 가장 많이 언급된 기업
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def hottestcorp(request):
    #어제부터 오늘
    startdate = date.today() - timedelta(days=1)
    enddate = date.today()
    news = get_object_or_404(
        News.objects.filter(date__range=[startdate, enddate]).annotate(count=Count('corporate_id')).order_by('-count')[:1]
    )
    corp_id = news.corporate_id
    corp = get_object_or_404(Corporate, pk=corp_id)
    serializer = CorporateSerializer(corp)

    return Response(serializer.data)


#유저 스크랩 수가 가장 많은 기업
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def popularcorp(request):
    corp = get_object_or_404(Corporate.objects.order_by('-scrap_cnt')[:1])
    serializer = CorporateSerializer(corp)
    
    return Response(serializer.data)

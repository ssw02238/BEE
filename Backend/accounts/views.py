#status & object
from os import stat
from django.core.checks import messages
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect, HttpResponse
from django.conf import settings

# rest api
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

# model
from django.contrib.auth import get_user_model
from .models import MBTI, UserManager
from corporates.models import Corporate
from .serializers import UserSerializer, PasswordSerializer, MbtiSerializer
from corporates.seiralizers import CorporateSerializer


#Authentication & Authorization
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# mbti
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from sqlalchemy import create_engine
import pymysql

# Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(methods=['post'], request_body=UserSerializer, responses={201: '성공', 400: '비밀번호 불일치', 409: '이메일 중복'})
@api_view(['POST'])
def signup(request):
    User = get_user_model()
    # 비밀번호 불일치 status code : 400
    password = request.data.get('password')
    password_confirmation = request.data.get('password_confirmation')

    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    # 이메일 중복 status code : 409
    email = request.data.get('email')
    try:
        exist_email = User.objects.get(email=email)
    except:
        exist_email = None

    if not exist_email is None:
        return Response({'error': '이미 존재하는 email 입니다.'}, status=status.HTTP_409_CONFLICT)

    # 유효성 검사 및 DB 저장 status code : 201
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

# password 변경


@swagger_auto_schema(methods=['put'], request_body=PasswordSerializer, 
                        manual_parameters=[openapi.Parameter('header_test', openapi.IN_HEADER, 
                            description="a header for  test", type=openapi.TYPE_STRING)])
@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def password(request):
    # 비밀번호 불일치 status code : 400
    password = request.data.get('password')
    password_confirmation = request.data.get('password_confirmation')

    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = PasswordSerializer(request.user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.save()
        return Response({'message': '성공적으로 변경되었습니다.'}, status=status.HTTP_200_OK)

# 마이페이지


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    User = get_user_model()
    client = request.user
    client_email = request.user.email

    if MBTI.objects.filter(user=client):
        mbti_score = [client.mbti.e_score, client.mbti.s_score, client.mbti.g_score]
    else:
        mbti_score = []

    client_object = get_object_or_404(get_user_model(), email=client_email)
    corporates_serializer = CorporateSerializer(
        client.scrap_corporates.all(), many=True)
    client_info = {
        'nickname': client_object.nickname,
        'email': client_email,
        'id': client.pk,
        'corporates': corporates_serializer.data,
        'mbti': mbti_score,
    }
    return JsonResponse(client_info, status=status.HTTP_200_OK)


# mbti 점수 저장 & 추천 기업 저장
@swagger_auto_schema(methods=['post', 'put'], request_body=MbtiSerializer)
@api_view(['POST', 'PUT',])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def mbti(request):
    User = get_user_model()
    user = request.user
    
    # 처음 했을 때 새로 저장
    if request.method == 'POST':
        serializer = MbtiSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
    
    # 다시 했을 때 수정해서 저장
    elif request.method == 'PUT':
        test = get_object_or_404(MBTI, user=user)
        serializer = MbtiSerializer(test, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # DB 불러와서 유사도 분석 후 temp 테이블에 결과 저장
    db_connection_str = 'mysql+pymysql://admin:1q2w3e4r5t!@bee.cjkrtt0iwcwz.ap-northeast-2.rds.amazonaws.com/BEE'
    db_connection = create_engine(db_connection_str)

    corp_query = "SELECT E_rating, S_rating, G_rating FROM corporates_corporate"
    corp_df = pd.read_sql(corp_query, db_connection)

    # user_query = f'SELECT e_score, s_score, g_score FROM accounts_mbti WHERE user_id={request.user.id}'
    user_query = f'SELECT e_score, s_score, g_score FROM accounts_mbti WHERE user_id={user.id}'
    user_df = pd.read_sql(user_query, db_connection)
    print(user_df)

    # 코사인 유사도가 높은 20개 기업 순서대로 출력
    cos_sim = cosine_similarity(user_df, corp_df)
    cos_sim_rank = cos_sim.argsort()[0,::-1][:20]
    cos_sim_corps = corp_df.iloc[cos_sim_rank]

    # 코사인 유사도 상위 20개 기업에 대해 유클리디안 거리 비교 및 상위 3개 출력
    sim_dist = euclidean_distances(user_df, cos_sim_corps)
    dist_sim_rank = sim_dist.argsort()[0][:3]
    dist_sim_corps = cos_sim_corps.index[dist_sim_rank]
    
    # 결과 저장
    user_mbti = user.mbti
    user_mbti.first = dist_sim_corps[0]
    user_mbti.second = dist_sim_corps[1]
    user_mbti.third = dist_sim_corps[2]
    user_mbti.save()
    
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile_esg(request):
    User = get_user_model()
    client = request.user

    if MBTI.objects.filter(user=client):
        mbti_score = {
            'e_score': client.mbti.e_score,
            's_score': client.mbti.s_score,
            'g_score': client.mbti.g_score,
        }
        recommend = [
            CorporateSerializer(get_object_or_404(Corporate, id=client.mbti.first)).data,
            CorporateSerializer(get_object_or_404(Corporate, id=client.mbti.second)).data,
            CorporateSerializer(get_object_or_404(Corporate, id=client.mbti.third)).data,
        ]
    else:
        mbti_score = []
        recommend = CorporateSerializer(Corporate.objects.order_by('-ESG_rating')[:3], many=True).data

    # corporates_serializer = CorporateSerializer(
    #     client.scrap_corporates.all(), many=True)
    client_info = {
        'mbti': mbti_score,
        'recommend': recommend,
    }
    return JsonResponse(client_info, status=status.HTTP_200_OK)

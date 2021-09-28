#status & object
from os import stat
from django.core.checks import messages
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect, HttpResponse
from django.conf import settings

#rest api
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

#model
from django.contrib.auth import get_user_model
from .models import UserManager
from .serializers import UserSerializer, PasswordSerializer
from corporates.seiralizers import CorporateSerializer

#Authentication & Authorization
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


@api_view(['POST'])
def signup(request):
    User = get_user_model()
    #비밀번호 불일치 status code : 400
    password = request.data.get('password')
    password_confirmation = request.data.get('password_confirmation')

    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    #이메일 중복 status code : 409
    email = request.data.get('email')
    try:
        exist_email = User.objects.get(email=email)
    except:
        exist_email = None
    
    if not exist_email is None:
        return Response({'error': '이미 존재하는 email 입니다.'}, status=status.HTTP_409_CONFLICT)
    
    #유효성 검사 및 DB 저장 status code : 201
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

#password 변경
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

#마이페이지 
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    User = get_user_model()
    client = request.user
    client_email = request.user.email

    client_object = get_object_or_404(get_user_model(), email=client_email)
    corporates_serializer = CorporateSerializer(client.scrap_corporates.all(), many=True)
    client_info = {
        'nickname': client_object.nickname,
        'email': client_email,
        'corporates': corporates_serializer.data,
    }
    return JsonResponse(client_info, status=status.HTTP_200_OK)


# mbti 점수 저장 
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def mbti(request):
    User = get_user_model()
    client = request.user
    client.e_score = request.data.get('e_score')
    client.s_score = request.data.get('s_score')
    client.g_score = request.data.get('g_score')
    client.save()


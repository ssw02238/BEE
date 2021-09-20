#status & object
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect, HttpResponse
from django.conf import settings

#rest api
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

#model
from .models import User
from django.contrib.auth import get_user_model

#Authentication & Authorization
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

@api_view(['POST'])
def signup(request):
    #비밀번호 일치, 불일치
    #중복된 이메일
    pass

@api_view(['PUT'])
def password(request):
    pass

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    pass
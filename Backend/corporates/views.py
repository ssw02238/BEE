#status & object
from django.core.checks import messages
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect, HttpResponse

#rest api
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

#model & serializing
from .models import Corporate
from .seiralizers import CorporateSerializer

# Create your views here.
@api_view(['GET'])
def corp_detail(request, corp_id):
    corp = get_object_or_404(Corporate, corp_id=corp_id)
    corp_serializer = CorporateSerializer(corp)
    pass

@api_view(['GET'])
def corp_news(request, corp_id):
    pass

#유사 기업
@api_view(['GET'])
def similar_corp(request, corp_id):
    pass

@api_view(['POST'])
def add_scrap(request, corp_id):
    pass

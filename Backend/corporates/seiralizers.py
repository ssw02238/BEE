from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Corporate, Environment, Social, Governance, News


# 환경 평가 내용
class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = '__all__'
        read_only_fields = ('corporate',)

# 사회 평가 내용
class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'
        read_only_fields = ('corporate',)

# 지배구조 평가 내용
class GovernanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governance
        fields = '__all__'
        read_only_fields = ('corporate',)

#기업 뉴스 
class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = ('title', 'content', 'url',)
        read_only_fields = ('corporate',)

# 기업 Detail
class CorporateDetailSerializer(serializers.ModelSerializer):
    environment_evaluation = EnvironmentSerializer(read_only=True, source="environment_set")
    social_evaluation = SocialSerializer(read_only=True, source="social_set")
    governance_evaluation = GovernanceSerializer(read_only=True, source="governance_set")
    news = NewsSerializer(read_only=True, many=True, source="news_set")
    # scrap cnt 추가해야함

    class Meta:
        model = Corporate
        fields = ('name', 'E_rating', 'S_rating', 'G_rating', 'ESG_rating',)


# 유사 기업 & 기업 검색 등 기업의 대략적인 정보만
class CorporateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Corporate
        fields = ('name', 'E_rating', 'S_rating', 'G_rating', 'ESG_rating',)
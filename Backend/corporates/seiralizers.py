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
        fields = ('title', 'content', 'url', 'date', 'corporate',)
        read_only_fields = ('corporate',)

# 기업 Detail
class CorporateDetailSerializer(serializers.ModelSerializer):
    environment_evaluation = EnvironmentSerializer(many=True, read_only=True, source="environment_set")
    social_evaluation = SocialSerializer(many=True, read_only=True, source="social_set")
    governance_evaluation = GovernanceSerializer(many=True, read_only=True, source="governance_set")
    news = NewsSerializer(many=True, read_only=True, source="news_set")

    class Meta:
        model = Corporate
        fields = '__all__'


class HottestCorpSerializer(serializers.ModelSerializer):
    news = NewsSerializer(many=True, read_only=True, source="news_set")
    
    class Meta:
        model = Corporate
        fields = ('name', 'pk', 'E_rating', 'S_rating', 'G_rating', 'ESG_rating', 'news')


# ESG 랭킹, 유사 기업 & 기업 검색 등 기업의 대략적인 정보만
class CorporateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Corporate
        fields = ('name', 'pk', 'E_rating', 'S_rating', 'G_rating', 'ESG_rating',)
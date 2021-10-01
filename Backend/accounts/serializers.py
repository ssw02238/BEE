from os import read
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import MBTI

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'nickname')


class PasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('password',)
        read_only_fields = ('email', 'nickname',)


class MbtiSerializer(serializers.ModelSerializer):

    class Meta:
        model = MBTI
        fields = ('id', 'e_score', 's_score', 'g_score', 'first', 'second', 'third',)
        read_only_fields = ('user',)

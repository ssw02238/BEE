from os import read
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

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
    e_score = serializers.FloatField(write_only=True)
    s_score = serializers.FloatField(write_only=True)
    g_score = serializers.FloatField(write_only=True)

    class Meta:
        model = User
        fields = ('e_score', 's_score', 'g_score',)
        read_only_fields = ('email', 'nickname', 'password')


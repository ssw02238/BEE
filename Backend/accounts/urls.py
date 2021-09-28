from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    path('signup/', views.signup),
    #로그인
    path('api-token-auth/', obtain_jwt_token),
    path('password/', views.password),
    path('profile/', views.profile),
    # mbti 점수 기록 
    path('mbti/', views.mbti)
]

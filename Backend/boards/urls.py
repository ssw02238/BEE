from django.urls import path

from . import views

urlpatterns = [
    path('esg-ranking', views.esg_ranking),
]

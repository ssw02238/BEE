from django.urls import path

from . import views

urlpatterns = [
    path('<str:corp_id>/detail/', views.detail)
]
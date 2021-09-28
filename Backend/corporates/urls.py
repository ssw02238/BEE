from django.urls import path

from . import views

urlpatterns = [
    path('<str:corp_id>/detail/', views.corp_detail),
    path('<str:corp_id>/news/', views.corp_news),
    path('<str:corp_id>/similarcorp/', views.similar_corp),
    path('<str:corp_id>/scrap/', views.add_scrap),
    path('search/<str:corp_name>/', views.search),
    path('similarity/', views.similarity),
]
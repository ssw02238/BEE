from django.urls import path

from . import views

urlpatterns = [
    path('esg-ranking/', views.esg_ranking),
    path('e-ranking/', views.e_ranking),
    path('s-ranking/', views.s_ranking),
    path('g-ranking/', views.g_ranking),
    path('bestcorp/', views.bestcorp),
    path('hottestcorp/', views.hottestcorp),
    path('popularcorp/', views.popularcorp),
]

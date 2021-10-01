from django.contrib import admin
from django.urls import path, include

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from rest_framework import permissions

# swagger 정보 설정, 관련 엔드포인트 추가
schema_view = get_schema_view(
    openapi.Info(
        title="BEE's API", # 타이틀
        default_version='v1', # 버전
        description="Best ESG Enterprise", # 설명
        terms_of_service="https://www.ssafy.com/ksp/jsp/swp/swpMain.jsp",
        contact=openapi.Contact(email="qkdwlghks00@gmail.com"),
        license=openapi.License(name="SSAFY License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('boards/', include('boards.urls')),
    path('corporates/', include('corporates.urls')),
]


# swagger 엔드포인트는 DEBUG Mode에서만 노출
if settings.DEBUG: urlpatterns += [ 
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
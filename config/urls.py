from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import TokenRefreshView

schema_view = get_schema_view(
   openapi.Info(
      title="Face Identificator API",
      default_version='v1',
      description="Face recognition va foydalanuvchi ro‘yxatdan o‘tish API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="your-email@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('identificator.urls')),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-schema'),
]
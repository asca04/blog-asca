from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),

    path('api/v1/user/', include('account.api.v1.urls')),
    path('api/v1/app/', include('app.api.v1.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('drf_social_oauth2.urls'), name='social_oauth2'),

    path('swagger<json>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

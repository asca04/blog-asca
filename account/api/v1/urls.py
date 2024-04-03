from django.urls import path

from account.api.v1.generic_views import UserCreateAPIView, CustomAuthToken

urlpatterns = [
    path('create', UserCreateAPIView.as_view(), name='user_create'),
    path('token', CustomAuthToken.as_view(), name='user_login'),
]
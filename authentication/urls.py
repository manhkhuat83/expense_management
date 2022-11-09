from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.views import UserRegisterView, SelfInfoView


urlpatterns = [
    path("token/auth", TokenObtainPairView.as_view()),
    path("token/refresh", TokenRefreshView.as_view()),
    path("user/self", SelfInfoView.as_view()),
    path("user/register", UserRegisterView.as_view()),
]

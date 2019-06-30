from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserCreateView, LoginView


urlpatterns = [
    path("users/", UserCreateView.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]

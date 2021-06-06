from django.conf.urls import include, url
from django.urls import path
from . import views
from core.views import UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register('user',UserViewSet)
urlpatterns = [
    path('',include(router.urls))
]
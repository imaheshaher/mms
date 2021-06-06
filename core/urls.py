from core.views.userview import CustomerViewSet
from django.db.models import base
from core.views.infoview import CustomerSubscriptionViewSet, MenuViewSet, MessSubscriptionViewSet, MessViewSet
from django.conf.urls import include, url
from django.urls import path
from . import views
from core.views import UserViewSet,UserApiView, MessViewSet ,MessSubscriptionViewSet,MenuViewSet,CustomerSubscriptionViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register('user',UserViewSet)
router.register('info/mess',MessViewSet,basename="mess")
router.register('info/menu',MenuViewSet,basename='menu')
router.register('info/msubscription',MessSubscriptionViewSet,basename='msubscription')
router.register('info/custsubscription',CustomerSubscriptionViewSet,basename='custsubsription')

urlpatterns = [
    path('',include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',UserApiView.as_view(),name='register'),
    path('register/<slug:pk>',UserApiView.as_view(),name='register_detail'),
    path('customer/',CustomerViewSet.as_view(),name='customer')

]
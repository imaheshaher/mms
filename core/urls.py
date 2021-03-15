from django.conf.urls import include, url
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r'menu', views.MenuViewset)
# router.register(r'feedback', views.FeedbackViewset)
router.register(r'present', views.PresentViewset)


urlpatterns =[
    path('',include(router.urls)),
    path('register/',views.RegisterApiview.as_view()),
    path('feedback/apiview/',views.FeedbackApiview.as_view()),
    path('loginview/',views.LoginView.as_view()),
    path('checklogin/',views.check_login)
]
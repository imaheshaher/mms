from core.models import Mess,Menu,CustomerSubscription,MessSubscription

from core.serializers import *
from rest_framework.response import Response

from core.utils import MyModelViewSet
from rest_framework.viewsets import ModelViewSet

class MessViewSet(ModelViewSet):
    serializer_class=MessSerializer
    queryset= Mess.objects.all()

class MenuViewSet(ModelViewSet):
    serializer_class=MenuSerializer
    queryset= Menu.objects.all()

class MessSubscriptionViewSet(ModelViewSet):
    serializer_class=MessSubsriptionSerializer
    queryset= MessSubscription.objects.all()

class CustomerSubscriptionViewSet(ModelViewSet):
    serializer_class=CustomerSubsriptionSerializer
    queryset= CustomerSubscription.objects.all()
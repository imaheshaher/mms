from core.models import Mess,Menu,CustomerSubscription,MessSubscription

from core.serializers import *
from rest_framework.response import Response

from core.utils import MyModelViewSet
from rest_framework.viewsets import ModelViewSet

class MessViewSet(ModelViewSet):
    serializer_class=MessSerializer
    model = Mess

class MenuViewSet(ModelViewSet):
    serializer_class=MenuSerializer
    model = Menu

class MessSubscriptionViewSet(ModelViewSet):
    serializer_class=MessSubsriptionSerializer
    model = MessSubscription

class CustomerSubscriptionViewSet(ModelViewSet):
    serializer_class=CustomerSubsriptionSerializer
    model = CustomerSubscription
from rest_framework.serializers import ModelSerializer
from core.models import *

class MessSerializer(ModelSerializer):
    class Meta:
        model=Mess
        fields="__all__"



class MenuSerializer(ModelSerializer):
    class Meta:
        model=Menu
        fields="__all__"

        
class MessSubsriptionSerializer(ModelSerializer):
    class Meta:
        model=MessSubscription
        fields="__all__"


class CustomerSubsriptionSerializer(ModelSerializer):
    class Meta:
        model=CustomerSubscription
        fields="__all__"

        
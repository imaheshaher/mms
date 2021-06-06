from core.models import User

from rest_framework.response import Response
from core.utils import MyAPIView
from core.utils.viewsets import MyModelViewSet
from core.serializers import UserSerialilzer
from rest_framework.viewsets import ModelViewSet

class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerialilzer




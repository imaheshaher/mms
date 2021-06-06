from rest_framework import serializers
from rest_framework.utils import field_mapping

from core.models import User

class UserSerialilzer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

        
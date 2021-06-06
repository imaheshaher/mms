from django.db.models import fields
from core import models
from core.models.usermodel import Customer
from re import L
from rest_framework import serializers
from rest_framework.utils import field_mapping

from core.models import User

class UserSerialilzer(serializers.ModelSerializer):
    customer=serializers.BooleanField('get_customer')
    def get_customer(self,user):
        print('user----',user)
        return user

    class Meta:
        model=User
        fields=('customer','email','password','name','mobile_number')

        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance




class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerialilzer(read_only=True)
    class Meta:
        model= Customer
        fields="__all__"
from django.db import models
from django.db.models import fields
from django.db.models.fields import files
from django.db.models.query_utils import FilteredRelation
from rest_framework import serializers
from .models import Feedback, Menu, Present_Customer, User,Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("mobile_number","course_name","joined_date")
class UserSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = User
        fields = ('first_name','last_name','username','password','customer')

    def create(self, validated_data):
        customer = validated_data.pop("customer")
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Customer.objects.create(user=user,**customer)
        return user



class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"



class PresentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Present_Customer
        fields = "__all__"

class FeedbackSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    menu = MenuSerializer(read_only=True)
    class Meta:
        model = Feedback
        fields = ("feedback","menu","customer")
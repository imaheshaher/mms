from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models.aggregates import Max
from django.contrib.auth.models import AbstractUser, PermissionsMixin
# Create your models here.
from django.utils.translation import ugettext_lazy as _
import uuid
from core.models.managers import UserManager
class User(AbstractBaseUser,PermissionsMixin):
    id=models.CharField(max_length=200,primary_key=True,default=uuid.uuid1)
    email = models.EmailField(_('email adderss'),unique=True)
    mobile_number = models.CharField(max_length=30,null=True,blank=True)
    name= models.CharField(max_length=300)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects=UserManager()



# class Menu(models.Model):
#     menu_name = models.CharField(max_length=30,blank=True,null=True)
#     meal_type = models.CharField(max_length=40,choices=MEAL_TYPE)
#     menu_date = models.DateField(null=True,blank=True)

#     def __str__(self) -> str:
#         return str(self.menu_name)
# class Customer(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     mobile_number = models.CharField(max_length=15,blank=True,null=True,unique=True)
#     course_name = models.CharField(max_length=20,blank=True,null=True)
#     joined_date = models.DateField(auto_now_add=True)


#     def __str__(self) -> str:
#         return "{}".format(self.user)



# class Present_Customer(models.Model):
#     menu = models.ForeignKey(Menu,on_delete=models.CASCADE,blank=True,null=True)
#     customer = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)

#     def __str__(self) -> str:
#         return str(self.customer)


# class Feedback(models.Model):
#     menu = models.ForeignKey(Menu,on_delete=models.CASCADE,blank=True,null=True)
#     customer = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)
#     feedback = models.TextField(blank=True,null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

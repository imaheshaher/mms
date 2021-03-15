from django.db import models
from django.db.models.aggregates import Max
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils.translation import ugettext_lazy as _

MEAL_TYPE = (
    ('breakfast','breakfast'),
    ('lunch','lunch'),
    ('dinner','dinner')
)

class User(AbstractUser):
    is_active=models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.username)
    # def create_superuser(self, username, password, **extra_fields):
    #     print("this is called")
    #     """
    #     Create and save a SuperUser with the given email and password.
    #     """
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #     extra_fields.setdefault('is_active', True)

    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError(_('Superuser must have is_staff=True.'))
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError(_('Superuser must have is_superuser=True.'))
    #     return self.create_user(username, password, **extra_fields)

class Menu(models.Model):
    menu_name = models.CharField(max_length=30,blank=True,null=True)
    meal_type = models.CharField(max_length=40,choices=MEAL_TYPE)
    menu_date = models.DateField(null=True,blank=True)

    def __str__(self) -> str:
        return str(self.menu_name)
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15,blank=True,null=True,unique=True)
    course_name = models.CharField(max_length=20,blank=True,null=True)
    joined_date = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return "{}".format(self.user)



class Present_Customer(models.Model):
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,blank=True,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self) -> str:
        return str(self.customer)


class Feedback(models.Model):
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,blank=True,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)
    feedback = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
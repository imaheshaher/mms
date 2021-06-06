from django.db import models
from core.models.usermodel import Customer, Vendor
import uuid
MENU_TYPE = (
    ('Breakfast','Breakfast'),
    ('Lunch','Lunch'),
    ('Dinner','Dinner')
)
SUB_TYPE = (
     ('oneday','oneday'),
     ('weekly','weekly'),
     ('monthly','monthly')
 )
SUB_STATUS  = (
    ('approve','approve'),
    ('reject','reject'),
    ('pending','pending')
)
class Mess(models.Model):
    id=models.CharField(max_length=200,primary_key=True,default=uuid.uuid1)

    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    mess_name = models.CharField(max_length=250,blank=True,null=True)
    is_veg = models.BooleanField(default=True)
    is_nonveg = models.BooleanField(default=True)
    is_mix = models.BooleanField(default=True)



class Menu(models.Model):
    id=models.CharField(max_length=200,primary_key=True,default=uuid.uuid1)

    mess = models.ForeignKey(Mess,on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=120,blank=True,null=True)
    menu_type=models.CharField(choices=MENU_TYPE,max_length=200)
    menu_date = models.DateField()


class MessSubscription(models.Model):
    id=models.CharField(max_length=200,primary_key=True,default=uuid.uuid1)

    mess = models.ForeignKey(Mess,on_delete=models.CASCADE)
    subscription_type = models.CharField(choices=SUB_TYPE,max_length=200)
    price = models.PositiveIntegerField()



class CustomerSubscription(models.Model):
    id=models.CharField(max_length=200,primary_key=True,default=uuid.uuid1)
    customer = models.ForeignKey(Customer,models.CASCADE)
    mess = models.ForeignKey(Mess,on_delete=models.CASCADE)
    subscription = models.ForeignKey(MessSubscription,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    sub_status=models.CharField(choices=SUB_STATUS,max_length=250,default='pending')
    total_price = models.PositiveIntegerField()

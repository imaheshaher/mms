from core.models import Customer, Feedback, Menu, User
from django.contrib import admin

# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(Feedback)
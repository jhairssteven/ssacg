from django.contrib import admin
from .models.client import Client
from .models.order import Order

# Register your models here.
admin.site.register(Client)
admin.site.register(Order)
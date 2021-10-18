from django.contrib import admin
from .models.users import Users
from .models.clients import Clients
from .models.admins import Admins
from .models.products import Products
from .models.orders import Orders
from .models.orders_detail import Orders_detail

# Register your models here.
admin.site.register(Users)
admin.site.register(Clients)
admin.site.register(Admins)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Orders_detail)

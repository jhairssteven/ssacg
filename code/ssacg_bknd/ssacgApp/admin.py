from django.contrib import admin
from .models.users import Users
from .models.clients import Clients
from .models.admins import Admins
from .models.products import Products

# Register your models here.
admin.site.register(Users)
admin.site.register(Clients)
admin.site.register(Admins)
admin.site.register(Products)

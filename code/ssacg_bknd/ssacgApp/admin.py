from django.contrib import admin
from .models.user import User
from .models.client import Client
from .models.admin import Admin

# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Admin)

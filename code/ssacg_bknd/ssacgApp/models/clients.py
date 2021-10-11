from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from .users import Users


class ClientManager(BaseUserManager):
    def create_user(self, name, email, password, address = "", phone = ""):
        if name is None:
            raise TypeError('You must enter a name')
        if email is None:
            raise TypeError('You must enter an email')
        if password is None:
            raise TypeError('You must enter a password, be secured')

        # email normalization to prevent multiple sign up
        user = self.model(name = name, email=self.normalize_email(email), 
                        address = address, phone = phone)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class Clients(Users):
    address = models.CharField('Shipping address', max_length=30, null=True)
    phone = models.CharField(max_length=20, null=True)
    
    objects = ClientManager()
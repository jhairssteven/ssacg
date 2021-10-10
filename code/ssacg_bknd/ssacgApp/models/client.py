from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueErro('Users must have an email bro')
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password,)
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class Client (AbstractBaseUser, PermissionsMixin):
    id_client = models.BigAutoField(primary_key=True)
    name = models.CharField('Clients name', max_length=15, null=True)
    email = models.EmailField('Client sign up email', max_length=50, unique=True)
    password = models.CharField('Password', max_length=256)
    address = models.CharField('Shipping address', max_length=30)
    phone = models.CharField('Client phone number', max_length=20, null=True)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdI3dlkajdfJOIjN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'email'

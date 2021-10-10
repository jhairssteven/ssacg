from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):

        if not username:
            raise ValueError('Users must have an username bro')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password,)
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class Client (AbstractBaseUser, PermissionsMixin):
    id_cliente = models.BigAutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=20)
    address = models.CharField('Address', max_length=50)
    phoneNumber = models.CharField('Phone_Number', max_length=12)
    password = models.CharField('Password', max_length=256)
    email = models.EmailField('Correo', max_length=100, unique=True)
    last_connection = models.DateTimeField()

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdI3dlkajdfJOIjN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'email'

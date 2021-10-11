from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, name, email, password):
        if name is None:
            raise TypeError('You must enter a name')
        if email is None:
            raise TypeError('You must enter an email')
        if password is None:
            raise TypeError('You must enter a password, be secured')

        # email normalization to prevent multiple sign up
        user = self.model(name = name, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.is_admin = True
        user.save()

        return user

class Users(AbstractBaseUser, PermissionsMixin):
    id_user = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=15, unique=False, default="My username")

    #set as primary key cause db_index & unique = True is unique
    email = models.EmailField(db_index=True, unique=True)
    password = models.CharField(max_length=256)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vygtdI3dlkajdfJOIjN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    # The 'USERNAME_FIELD' tells us the field we we will use to log in and identify uniquely each user
    USERNAME_FIELD = 'email'

    # A list of the required fields when creating a superuser via the terminal
    REQUIRED_FIELDS = ['name', 'password']

    objects = UserManager()


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .choice import *


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, user_id, password, email, dob,  phone, name, address, auth, **extra_fields):
        user = self.model(
                user_id = user_id,
                email = email,
                dob = dob,
                phone = phone,
                name = name,
                address = address,
                auth = auth,
                **extra_fields
                )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, user_id, password, email=None, dob=None,  phone=None, name=None, address=None, auth=None):
        user = self.create_user(user_id, password, email, dob,  phone, name, address, auth)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.level = 0
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

        objects = UserManager()

        user_id = models.CharField(max_length = 17, verbose_name = "ID", unique = True)
        password = models.CharField(max_length = 256, verbose_name = "Password")
        dob = models.DateField(max_length = 10, verbose_name = "Date_of_Birth", null = True)
        email = models.EmailField(max_length = 128, verbose_name = "Email", null = True, unique = True)
        phone = models.IntegerField(verbose_name = "Phone", null=True, unique = True)
        name = models.CharField(max_length = 17, verbose_name = "Full Name", null = True)
        address = models.CharField(max_length = 128, verbose_name = "Home Address", null = True)
        level = models.CharField(max_length =17, verbose_name = "level", default = 3)
        auth = models.CharField(max_length = 10, verbose_name = "Auth Code", null = True)

        is_active = models.BooleanField(default = True)
        is_admin = models.BooleanField(default = False)
        is_staff = models.BooleanField(default = False)
        is_superuser = models.BooleanField(default = False)
        date_joined = models.DateTimeField(auto_now_add = True)

        USERNAME_FIELD = 'user_id'
        REQUIRED_FIELDS = ['email']

        def __str__(self):
            return self.user_id

        class Meta:
           db_table = "User_List"
           verbose_name = "User"
           verbose_name_plural = "Users"


# Create your models here.

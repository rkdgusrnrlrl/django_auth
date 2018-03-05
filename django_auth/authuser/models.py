from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager



class AuthUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("User must have an email")

        authuser = self.model(email=email, name=name)
        authuser.set_password(password)
        authuser.save()
        return authuser

    def create_superuser(self, email, name, password):
        authuser = self.model(email=email, name=name, password=password)
        authuser.is_admin = True
        authuser.save()

class AuthUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AuthUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    @property
    def hello(self):
        return self.name + " hello"

    @property
    def is_staff(self):
        return self.is_admin

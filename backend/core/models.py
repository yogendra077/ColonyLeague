from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.conf import settings
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fileds):
        if not email:
            raise ValueError('User needs an email address')
        user=self.model(email=self.normalize_email(email),**extra_fileds)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        user=self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects= UserManager()

class Team(models.Model):
    teamName = models.CharField(max_length=255)
    player = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    teamSize = models.IntegerField(default=0)
    
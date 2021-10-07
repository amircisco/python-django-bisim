from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import UserManager


class Account(AbstractBaseUser, PermissionsMixin):
    mobile = models.CharField(max_length=20, verbose_name='تلفن همراه', unique=True)
    email = models.CharField(max_length=200, verbose_name='ایمیل', blank=True, null=True)
    fullname = models.CharField(max_length=400, verbose_name='نام و نام خانوادگی', blank=True, null=True)
    is_superuser = models.BooleanField(default=False, verbose_name='مدیرکل')
    is_staff = models.BooleanField(default=False, verbose_name='کارمند')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    USERNAME_FIELD = 'mobile'
    objects = UserManager()

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'کابر'
        verbose_name_plural = 'کاربران'

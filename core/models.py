from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from .managers import UserManager
from django.contrib.auth.models import Group


class Company(models.Model):
    name = models.CharField(max_length=400, verbose_name='نام شرکت')
    address = models.TextField(max_length=1000, verbose_name='آدرس شرکت', blank=True,null=True)
    tel = models.CharField(max_length=100, verbose_name='تلفن های شرکت', blank=True,null=True)
    manager = models.ForeignKey('Member', on_delete=models.CASCADE, verbose_name='مدیر شرکت', related_name='manager')
    team_count = models.IntegerField(verbose_name='تعدا گروه های شرکت')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='تاریخ عضویت شرکت')

    class Meta:
        verbose_name='شرکت'
        verbose_name_plural = 'شرکت ها'

class Member(AbstractBaseUser, PermissionsMixin):
    mobile = models.CharField(max_length=20, verbose_name='تلفن همراه', unique=True)
    level = models.IntegerField(default=1)
    last_loc = models.CharField(max_length=100, verbose_name='اطلاعات آخرین مکان', blank=True,null=True)
    name = models.CharField(max_length=400, verbose_name='نام و نام خانوادگی')
    is_superuser = models.BooleanField(default=False, verbose_name='مدیرکل')
    is_staff = models.BooleanField(default=False, verbose_name='کارمند')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='تاریخ عضویت')

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['level']
    objects = UserManager()

    def __str__(self):
        return str(self.mobile) + str(self.name)

    class Meta:
        verbose_name='کابر'
        verbose_name_plural = 'کاربران'

class Team(models.Model):
    name = models.CharField(max_length=400, verbose_name='نام گروه')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='نام شرکت', related_name='company')
    team_manager = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='مدیر گروه', related_name='team_manager')
    team_owner = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='مدیر ارشد گروه', related_name='team_owner')
    team_members = models.ManyToManyField(Member, verbose_name='اعضای گروه', blank=True, related_name='team_members')
    black_list = models.ManyToManyField(Member, verbose_name='لیست سیاه', blank=True, related_name='black_list')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد گروه')

    class Meta:
        verbose_name='تیم(گروه)'
        verbose_name_plural = 'تیم ها(گروه ها)'

class Location(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='کاربر', related_name='users')
    year_month = models.CharField(max_length=50, verbose_name='ماه و سال')
    loc_data = models.CharField(max_length=200, verbose_name='اطلاعات مکان')

    class Meta:
        verbose_name='مکان کاربر'
        verbose_name_plural = 'مکان کاربران'
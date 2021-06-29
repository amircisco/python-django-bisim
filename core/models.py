from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from .managers import UserManager


class Company(models.Model):
    name = models.CharField(max_length=400, verbose_name='نام شرکت')
    address = models.TextField(max_length=1000, verbose_name='آدرس شرکت', blank=True,null=True)
    tel = models.CharField(max_length=100, verbose_name='تلفن های شرکت', blank=True,null=True)
    manager = models.ForeignKey('Members', on_delete=models.CASCADE, verbose_name='مدیر شرکت')
    team_count = models.IntegerField(max_length=4, verbose_name='تعدا گروه های شرکت')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='تاریخ عضویت شرکت')


class Member(AbstractBaseUser, PermissionsMixin):
    mobile = models.CharField(max_length=20, verbose_name='تلفن همراه', unique=True)
    level = models.IntegerField(max_length=3)
    last_loc = models.CharField(max_length=100, verbose_name='اطلاعات آخرین مکان', blank=True,null=True)
    name = models.CharField(max_length=400, verbose_name='نام و نام خانوادگی')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='تاریخ عضویت')

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return str(self.mobile) + str(self.name)


class Team(models.Model):
    name = models.CharField(max_length=400, verbose_name='نام گروه')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='نام شرکت')
    team_manager = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='مدیر گروه')
    team_owner = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='مدیر ارشد گروه')
    team_members = models.ManyToManyField(Member, verbose_name='اعضای گروه', blank=True,null=True)
    black_list = models.ManyToManyField(Member, verbose_name='لیست سیاه', blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد گروه')


class Location(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='کاربر')
    year_month = models.CharField(max_length=50, verbose_name='ماه و سال')
    loc_data = models.CharField(max_length=200, verbose_name='اطلاعات مکان')
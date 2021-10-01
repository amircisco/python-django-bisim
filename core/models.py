from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from account.models import Account
from django.contrib.auth.models import Group


class Company(models.Model):
    name = models.CharField(max_length=400, verbose_name='نام شرکت')
    address = models.TextField(max_length=1000, verbose_name='آدرس شرکت', blank=True, null=True)
    tel = models.CharField(max_length=100, verbose_name='تلفن های شرکت', blank=True, null=True)
    team_count = models.IntegerField(verbose_name='تعدا گروه های شرکت')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت شرکت')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'شرکت'
        verbose_name_plural = 'شرکت ها'


class Member(Account):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)  # levels: member=1 , team_manager = 3 , team_owner = 5
    last_loc = models.CharField(max_length=100, verbose_name='اطلاعات آخرین مکان', blank=True, null=True)

    def __str__(self):
        return str(self.mobile) + str(self.name)

    class Meta:
        verbose_name = 'عضو شرکت'
        verbose_name_plural = "اعضای شرکت ها"


class Team(models.Model):
    name = models.CharField(max_length=400, verbose_name='نام گروه')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='نام شرکت', related_name='company')
    team_manager = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='مدیر گروه',
                                     related_name='team_manager')
    team_owner = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='مدیر ارشد گروه',
                                   related_name='team_owner')
    team_members = models.ManyToManyField(Member, verbose_name='اعضای گروه', blank=True, related_name='team_members')
    black_list = models.ManyToManyField(Member, verbose_name='لیست سیاه', blank=True, related_name='black_list')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد گروه')

    class Meta:
        verbose_name = 'تیم(گروه)'
        verbose_name_plural = 'تیم ها(گروه ها)'


class Location(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='کاربر', related_name='users')
    year_month = models.CharField(max_length=50, verbose_name='ماه و سال')
    loc_data = models.CharField(max_length=200, verbose_name='اطلاعات مکان')

    class Meta:
        verbose_name = 'مکان کاربر'
        verbose_name_plural = 'مکان کاربران'

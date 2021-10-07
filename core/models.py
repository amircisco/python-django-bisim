from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from account.models import Account
from django.contrib.auth.models import Group


class Company(models.Model):
    name = models.CharField(max_length=400, verbose_name='نام شرکت')
    address = models.TextField(max_length=1000, verbose_name='آدرس شرکت', blank=True, null=True)
    tel = models.CharField(max_length=100, verbose_name='تلفن های شرکت', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت شرکت')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'شرکت'
        verbose_name_plural = 'شرکت ها'


class Member(models.Model):
    LEVLES = (('1','عضو'),('2','مدیر گروه'),('3','مدیر ارشد'))
    name = models.CharField(max_length=200, verbose_name='نام', unique=True)
    mobile = models.CharField(max_length=20, verbose_name='تلفن همراه', unique=True)    
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="members", verbose_name="نام شرکت")
    level = models.CharField(choices=LEVLES, max_length=2, verbose_name="نوع عضویت") 
    password = models.CharField(max_length=100, verbose_name="رمز عبور")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'عضو شرکت'
        verbose_name_plural = "اعضای شرکت ها"


class Team(models.Model):
    name = models.CharField(max_length=400, verbose_name='نام گروه')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='نام شرکت', related_name="temas")
    manager = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='مدیر گروه', related_name="managers_teams")
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='مدیر ارشد گروه', related_name="owners_teams")
    members = models.ManyToManyField(Member, verbose_name='اعضای گروه', blank=True)
    blacklist = models.ManyToManyField(Member, verbose_name='لیست سیاه', blank=True, related_name="blacklists_teams")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد گروه')

    class Meta:
        verbose_name = 'تیم(گروه)'
        verbose_name_plural = 'تیم ها(گروه ها)'

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="گروه")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name="عضو")


class Location(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='کاربر', related_name='users')
    locdate = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    locdata = models.CharField(max_length=200, verbose_name='اطلاعات مکان')

    class Meta:
        verbose_name = 'مکان کاربر'
        verbose_name_plural = 'مکان کاربران'

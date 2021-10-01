from django.contrib import admin
from core.models import Company,Team,Member,Location


class AdminCompany(admin.ModelAdmin):
    model = Company
    fields = ['name','address','tel','manager']
    list_display = ['name', 'manager', 'date_joined']



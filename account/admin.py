from django.contrib import admin
from .models import Account


class AdminAccount(admin.ModelAdmin):
    model = Account
    fields = [
        'mobile',
        'email',
        'fullname',
        'is_superuser',
        'is_staff',
        'is_active',
    ]
    list_display = [
        'mobile',
        'fullname',
    ]


admin.site.register(Account, AdminAccount)

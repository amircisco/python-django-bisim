from django.contrib import admin
from core.models import Company, Team, Member, Account, Location


class AdminCompany(admin.ModelAdmin):
    model = Company
    fields = [
        'name',
        'address',
        'tel',
        'team_count',
    ]
    list_display = [
        'name',
        'team_count',
        'date_joined',
        'team_count',
    ]


class AdminTeam(admin.ModelAdmin):
    model = Team
    fields = [
        'name',
        'company',
        'team_manager',
        'team_owner',
        'team_members',
        'black_list',
    ]
    list_dsiplay = [
        'name',
        'company',
        'team_manager',
    ]


class AdminAccount(admin.ModelAdmin):
    model = Account
    fields = [
        'mobile',
        'email',
        'fullname',
        'is_member',
        'is_superuser',
        'is_staff',
        'is_active',
    ]
    list_display = [
        'mobile',
        'fullname',
    ]


class AdminMember(admin.ModelAdmin):
    model = Member
    fields = [
        'company',
        'mobile',
        'email',
        'fullname',
        'is_member',
        'is_superuser',
        'is_staff',
        'is_active',
        'level',
        'last_loc',
    ]
    list_display = [
        'mobile',
        'fullname',
        'company',
    ]


admin.site.register(Company,AdminCompany)
admin.site.register(Team,AdminTeam)
admin.site.register(Account,AdminAccount)
admin.site.register(Member,AdminMember)
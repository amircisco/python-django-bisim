from django.contrib import admin
from core.models import Company, Team, Member, Location


class AdminCompany(admin.ModelAdmin):
    model = Company
    fields = [
        'name',
        'address',
        'tel',
    ]
    list_display = [
        'name',
        'team_count',
        'date_joined',
    ]

    def team_count(self, obj):
        return obj.members

    team_count.short_description = "تعداد تیم"

class AdminTeam(admin.ModelAdmin):
    model = Team
    fields = [
        'name',
        'company',
        'manager',
        'owner',
        'members',
        'blacklist',
    ]
    list_dsiplay = [
        'name',
        'company',
        'manager',
    ]


class AdminMember(admin.ModelAdmin):
    model = Member
    fields = [
        'name',
        'mobile',
        'company',
        'level',
    ]
    list_display = [
        'name',
        'mobile',
        'company',
        'level',
    ]


admin.site.register(Company,AdminCompany)
admin.site.register(Team,AdminTeam)
admin.site.register(Member,AdminMember)
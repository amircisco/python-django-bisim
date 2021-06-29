from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from core.models import Member


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username == None:
            username = kwargs.get('mobile')
        if len(username)==11 and username.isdigit():
            user = list(Member.objects.filter(Q(mobile=username)).values('id'))[0]
            if user:
                user = Member.objects.get(pk=user.get('id'))
                if user.check_password(password) and self.user_can_authenticate(user):
                    return user
        return None
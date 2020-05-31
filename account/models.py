import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now as time_zone_now


def upload_to(instance, filename):
    now = time_zone_now()
    base, ext = os.path.splitext(filename)
    ext = ext.lower()
    return f"users/{now:%Y/%m/%Y%m%d%H%M%S}{ext}"


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_num = models.CharField(blank=True, null=True, max_length=11)
    sex = models.CharField(max_length=2, choices=((1, '男'), (2, '女')), default=1)
    picture = models.FileField(blank=True, null=True, upload_to=upload_to)

    def __str__(self):
        return self.user.username

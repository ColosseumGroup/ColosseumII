from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField  # NOQA

# from django.contrib.auth.models import User
# Create your models here.

class AdminType(object):
    REGULAR_USER = "Regular User"
    ADMIN = "Admin"
    SUPER_ADMIN = "Super Admin"


class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=64, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    admin_type = models.CharField(max_length=32, default=AdminType.REGULAR_USER)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    game_status = JSONField(default=dict)
    # game_status examples:
    # {
    #     "reversi": {
    #         "1": {
    #             "opponent_id":"12345",
    #             "status": JudgeStatus.WON,
    #             "_id": "1000"
    #         }
    #     },
    #     "poker": {
    #         "1": {
    #             "opponent_1_id":"12345",
    #             "opponent_2_id":"12345",
    #             "opponent_3_id":"12345",
    #             "status": JudgeStatus.LOST,
    #             "_id": "1000"
    #         }
    #     }
    # }
    real_name = models.CharField(max_length=32, blank=True, null=True)
    # avatar = models.CharField(max_length=256, default="%s/default.png" % settings.AVATAR_URI_PREFIX)
    blog = models.URLField(blank=True, null=True)
    mood = models.CharField(max_length=256, blank=True, null=True)
    github = models.CharField(max_length=64, blank=True, null=True)
    school = models.CharField(max_length=64, blank=True, null=True)
    major = models.CharField(max_length=64, blank=True, null=True)

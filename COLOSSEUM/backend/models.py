from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField  # NOQA


class GameType(models.Model):
    game_name = models.CharField(max_length = 32)
    game_description = models.TextField()
    def __str__(self):
        return self.game_name

class Game(models.Model):
    STATUS = (
        ('0','Pending'),
        ('1','OnGoing'),
        ('2','Finished'),
        ('3','ErrrorUnfinished'),
    )
    game_type = models.ForeignKey(GameType,on_delete = models.CASCADE)
    status = models.CharField(max_length=1, choices = STATUS, default = '0')
    created_time = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ['created_time']
    

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    games = models.ManyToManyField(Game)
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
    submission_number = models.IntegerField(default = 0)
    win_number = models.IntegerField(default = 0)
    def add_win_problem_number(self):
        self.win_number = models.F("win_number") + 1
        self.save()
    def add_submission_number(self):
        self.submission_number = models.F("submission_number") + 1
        self.save()

class Result(models.Model):
    belong_to_game_id = models.IntegerField(default = 0)
    player = models.ForeignKey(User,on_delete = models.CASCADE)
    scores = models.IntegerField(default = 0)

class Steps(models.Model):
    belong_to_game_id = models.IntegerField(default = 0)    
    player = models.ForeignKey(User,on_delete = models.CASCADE)
    created_time = models.DateTimeField(auto_now_add = True)
    step_taken = models.IntegerField(default = 0)
    

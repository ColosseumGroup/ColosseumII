from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# class Game(models.Model):
#     trial = models.CharField(max_length = 50, default = "default")
#     def __str__(self):
#         return self.trial
    

class GameType(models.Model):
    game_name = models.CharField(max_length = 32)
    game_description = models.TextField()
    def __str__(self):
        return self.game_name

class Result(models.Model):
    user_1_score = models.IntegerField(default = 0)
    user_2_score = models.IntegerField(default = 0)
    user_3_score = models.IntegerField(default = 0)
    user_4_score = models.IntegerField(default = 0)


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
    players = models.ManyToManyField(User, through='JoinGame')
    result = models.ForeignKey(Result, on_delete = models.CASCADE)
    class Meta:
        ordering = ['created_time']

class JoinGame(models.Model):
    player = models.ForeignKey(User,on_delete = models.CASCADE)
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    join_time = models.DateTimeField(auto_now_add = True)

class Decision(models.Model):
    game = models.ForeignKey(Game, on_delete =models.CASCADE)
    created_time = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    decision_code = models.IntegerField(default = 0)
    def IsValid(self):
        pass

# # class UserProfile(models.Model):
# #     user = models.ForeignKey(User, on_delete = models.CASCADE)
# #     games = models.ManyToManyField(Game, blank = True )
# #     # game_status = JSONField(default=dict)
# #     # game_status examples:
# #     # {
# #     #     "reversi": {
# #     #         "1": {
# #     #             "opponent_id":"12345",
# #     #             "status": JudgeStatus.WON,
# #     #         }
# #     #     },
# #     #     "poker": {
# #     #         "1": {
# #     #             "opponent_1_id":"12345",
# #     #             "opponent_2_id":"12345",
# #     #             "opponent_3_id":"12345",
# #     #             "status": JudgeStatus.LOST,
# #     #             "_id": "1000"
# #     #         }
# #     #     }
# #     # }
# #     # real_name = models.CharField(max_length=32, blank=True, null=True)
# #     # avatar = models.CharField(max_length=256, default="%s/default.png" % settings.AVATAR_URI_PREFIX)
# #     # blog = models.URLField(blank=True, null=True)
# #     # github = models.CharField(max_length=64, blank=True, null=True)
# #     # school = models.CharField(max_length=64, blank=True, null=True)
# #     # major = models.CharField(max_length=64, blank=True, null=True)
# #     game_number = models.IntegerField(default = 0)
# #     win_number = models.IntegerField(default = 0)
# #     def add_win_problem_number(self):
# #         self.win_number = models.F("win_number") + 1
# #         self.save()
# #     def add_game_number(self):
# #         self.game_number = models.F("game_number") + 1
# #         self.save()

# # class Result(models.Model):
# #     belong_to_game_id = models.IntegerField(default = 0)
# #     result = JSONField(default = dict)
# #     # result examples:
# #     # {
# # #         "winner_id":"12346",     
# #         "user_1": {
# #             "user_id":"12345",
# #             "scores": "0",
# #         },
# #         "user_2": {
# #             "user_id":"12346",
# #             "scores": "2",
# #         },
#     # }    



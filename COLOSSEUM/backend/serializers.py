from rest_framework import serializers
from backend.models import User,Game,Decision# ,UserProfile,Result,Steps
from django import forms

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name')

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ('user','game_status','real_name','blog','mood','github','school','major')

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
    # username = serializers.CharField()
    # password = serializers.CharField()
    # tfa_code = serializers.CharField(required=False, allow_blank=True)
    # What's tfa_code? 

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('game_type', 'status','created_time')

class DecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decision
        fields = ('game', 'user', 'created_time', 'decision_code')
 
        
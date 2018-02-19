from rest_framework import serializers
from backend.models import User, UserProfile
from django import forms

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user','game_status','real_name','blog','mood','github','school','major')

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
    # username = serializers.CharField()
    # password = serializers.CharField()
    # tfa_code = serializers.CharField(required=False, allow_blank=True)
    # What's tfa_code? 

class UsernameOrEmailCheckSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=32)
    password = serializers.CharField(min_length=6)
    email = serializers.EmailField(max_length=64)
    captcha = serializers.CharField()

class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField(min_length=6)
    # tfa_code = serializers.CharField(required=False, allow_blank=True)

class UserChangeEmailSerializer(serializers.Serializer):
    password = serializers.CharField()
    new_email = serializers.EmailField(max_length=64)
    # tfa_code = serializers.CharField(required=False, allow_blank=True)

class GenerateUserSerializer(serializers.Serializer):
    prefix = serializers.CharField(max_length=16, allow_blank=True)
    suffix = serializers.CharField(max_length=16, allow_blank=True)
    number_from = serializers.IntegerField()
    number_to = serializers.IntegerField()
    password_length = serializers.IntegerField(max_value=16, default=8)
    # what's this for?



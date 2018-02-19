from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required,user_passes_test

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from backend.models import User,UserProfile
from backend.serializers import UserSerializer,UserProfileSerializer

@csrf_exempt    
def LoginAPI(req):
    # request = JSONParser().parse(req)
    if req.method == 'POST':
        username = req.POST.get("username")
        password = req.POST.get("password")
        # print(username, password)
        usr = authenticate(req,username = username, password = password)
        # serializer = UserSerializer(data = request)
        if usr is not None:
            login(req, usr)
            return HttpResponse(status = 200)
        else:
            return HttpResponse("You there! You're the bad guy!(>_<)", status = 400)
    elif req.method == 'GET':
            return HttpResponse("What the hell do you think you are doing?!",status = 403)

@csrf_exempt
@login_required
def LogoutAPI(req):
    if req.method == 'GET':
        logout(req)
        return HttpResponse("All right, see ya(｡･ω･)ﾉ", status = 200)

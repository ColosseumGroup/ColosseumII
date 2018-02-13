from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from backend.models import User,UserProfile
from backend.serializers import UserSerializer,UserProfileSerializer

@csrf_exempt
def UserProfileAPI(request):
    if request.method == 'GET':
        usr = User.objects.all()
        serializers = UserSerializer(usr,many = True)
        return JsonResponse(serializers.data,safe = False )

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required,user_passes_test

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from backend.models import User,Game,GameType
from backend.serializers import UserSerializer, DecisionSerializer

@csrf_exempt    
def LoginAPI(req):
    # request = JSONParser().parse(req)
    if req.method == 'POST':
        username = req.POST.get("username")
        password = req.POST.get("password")
        print(username, password)
        usr = authenticate(req,username = username, password = password)
        # serializer = UserSerializer(data = request)
        print(usr)
        if usr is not None:
            a = login(req, usr)
            print(a)
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

@csrf_exempt
def RegisterAPI(req):
    if req.method == 'GET':
        return HttpResponse(status = 201) # trial
    if req.method == 'POST':
        username = req.POST.get("username")
        password = req.POST.get("password")
        email = req.POST.get("email")
        first_name = req.POST.get("first_name")
        last_name = req.POST.get("last_name")
        if User.objects.all().filter(username = username) is None:
            return HttpResponse(status = 403)
        NewUser = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)
        NewUser.save()
        # user_profile = UserProfile(user = NewUser)
        # user_profile.save()
        return HttpResponse(status = 200)

@csrf_exempt
def CreateOthelloGameAPI(req):
    # if is_valid():
    if req.method == 'POST':
        game_type = GameType.objects.get(pk = 1)
        new_game = Game(game_type = game_type)
        new_game.save()
        return HttpResponse(new_game.id,status = 200)

@csrf_exempt
def GameInfoAPI(req,GameID):
    # game = Game.objects.get(pk = GameID)
    if req.method == 'POST':
        usr = req.user
        game = Game.objects.get(pk = GameID)
        if game.status != '0':
            join_game = JoinGame(player = usr, game = game)
            return HttpResponse(status = 200)  
        return HttpResponse(status = 403)
    elif req.method == 'GET':
        game = Game.objects.get(pk = GameID)
        return HttpResponse(game.status,status = 200)
    

@csrf_exempt
def GameStepsAPI(req,GameID):
    game = Game.objects.get(pk = GameID)
    if req.method == 'POST':
        usr = req.User
        decision_code = req.POST['decision_code']
        new_decision = Decision(game = game, user = usr, decision_code = decision_code)
        if new_decision.IsValid():
            new_decision.save()
            return HttpResponse(status = 200) 
        return HttpResponse("operation not valid",status = 400)
    elif req.method == 'GET':
        record = Decision.objects.all().filter(game.objects.get(pk  = GameID))
        serializer = DecisionSerializer(record, many = True)
        return JsonResponse(serializer.data, safe = False)

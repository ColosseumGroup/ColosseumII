from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from backend.models import User,Game,GameType,JoinGame
from backend.serializers import UserSerializer, DecisionSerializer
# from backend.interact import InteractWithGameServer

import json
import requests
import http
import urllib.parse

game_server_url = 'http://139.224.114.52'
port = 8081
default_headers ={
    "Content-Type":"application/json"
}
#new interact, using python lib 'request'
def InteractWithGameServer(dict_param = None, headers = default_headers,append_url='/',req='GET'):
    url = game_server_url+':'+str(port)+append_url
    if req == 'GET':
        response = requests.get(url,data=dict_param,headers=headers)
        result = str(response.json())
    elif req == 'POST':
        response = requests.post(url,data=json.dumps(dict_param),headers=headers)
        result = str(response.json())
    return eval(result)

@csrf_exempt    
def LoginAPI(req):# VALID
    # login api, req in the form of form-data
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        print(username, password)
        usr = authenticate(req,username = username, password = password)
        serializer = UserSerializer(data = req)
        print(serializer)
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
def LogoutAPI(req): # VALID
    #logout api
    if req.method == 'GET':
        a = logout(req)
        print(a)
        return HttpResponse("All right, see ya(｡･ω･)ﾉ", status = 200)

@csrf_exempt
def RegisterAPI(req):
    if req.method == 'GET':
        return HttpResponse(status = 201) # trial
    if req.method == 'POST':
        serializer = UserSerializer(data = req)
        print(serializer.is_valid())
        if serializer.is_valid():
            print(serializer)
        """
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
        """
        return HttpResponse(status = 200)


@csrf_exempt
@login_required
def CreateNewGameRoomAPI(req,GameTypeID): # VALID
    if req.method == 'POST':
        # user_port = req.POST['port']
        game_type = GameType.objects.get(pk = GameTypeID)
        new_game = Game(game_type = game_type)
        player = req.user
        new_game.save() 
        join = JoinGame(player = player, game = new_game)
        join.save()
        # new_game.players.add(join)
        return HttpResponse(new_game.id,status = 200)

@csrf_exempt
# @login_required
def GameInfoAPI(req,GameID):
    # POST - join game
    if req.method == 'POST':
        usr = req.user
        game = Game.objects.get(pk = GameID)
        players = game.players.all()
        dict_param = {
            'gameID': str(GameID),
            # 'game': game.game_type.game_name,
            'game': 'dealer_renju',
            'NPC': 'starter',
            'rounds':'1',
            'random_seed':'False',
            'game_define':'False',
            'players': [
                {'name_{}'.format(cnt+1) : player.username}
                for cnt,player in enumerate(players)
            ]
        }
        # DEV-NOTES:
        # the requests.post showed many an exception in this case
        # it first claimed that 
        # ('Connection aborted.', RemoteDisconnected('Remote end closed connection 
        # without response',)) 
        # I figured it was a problem with configuring user-agent, and used charles 
        # as a test, but nothing satisfying came up
        # After a series of tests casted independently on interact.py and views.py
        # it was finally discovered that the problem lay with json.dump
        # the original dict_param I offered as data in requests.post was not qualifed.
        if game.status == '0': # if there aren't still enough users in the game room
            join_game = JoinGame(player = usr, game = game)
            join_game.save() # enable join-room for current user
            # if the number of users in the room satisfy the requirements, change 
            # game.status and create game, sending the game information to the game 
            # server, and offering the returned ports to user
            if game.players.all().count() == game.max_player_num: 
                players = game.players.all()
                dict_param = {
                    'gameID': str(GameID),
                    # 'game': game.game_type.game_name,
                    'game': 'dealer_renju',
                    'NPC': 'starter',
                    'rounds':'1',
                    'random_seed':'False',
                    'game_define':'False',
                    'players': [
                        {'name_{}'.format(cnt+1) : player.username}
                        for cnt,player in enumerate(players)
                    ]
                }
                server_response = InteractWithGameServer(dict_param=dict_param, append_url='/api/play',req='POST')
                # further deal with 
                game.server_response = json.dumps(server_response)
                if server_response['status'] == "ongoing":
                    game.status = '1'
                game.save()
                return HttpResponse(json.dumps(dict_param)+json.dumps(server_response),status = 200)  
        return HttpResponse(json.dumps(game.server_response),status = 403)
    # GET - get game info & status
    elif req.method == 'GET':
        try:
            game = Game.objects.get(pk = GameID)
        except: # if there is no matching game ID
            return HttpResponse("ERR: GAME DOES NOT EXIST",status = 400)
        players = game.players.all()
        game_info = {
            'gameID':str(GameID),
            'game':'dealer_renju'
        }
        check_game = InteractWithGameServer(dict_param=game_info,append_url='/api/check',req='POST')
        return JsonResponse({
            'game_info': {
                'gameID': str(GameID),
                # 'game': game.game_type.game_name,
                'game': 'dealer_renju',
                'NPC': 'starter',
                'rounds':'1',
                'random_seed':'False',
                'game_define':'False',
                'players': [
                    {
                        'name_{}'.format(cnt+1) : player.username,
                        'port_{}'.format(cnt+1): json.loads(game.server_response)['ports']['player{}_port'.format(cnt)]
                    }
                    for cnt,player in enumerate(game.players.all())
                ]                
            },
            'current_status': check_game
        },status = 200)
        # RETURN-EXAMPLE
        # {
        #     "game_info": {
        #         "gameID": "16",
        #         "game": "dealer_renju",
        #         "NPC": "starter",
        #         "rounds": "1",
        #         "random_seed": "False",
        #         "game_define": "False",
        #         "players": [
        #             {
        #                 "name_1": "trial",
        #                 "port_1": "41703"
        #             },
        #             {
        #                 "name_2": "trial",
        #                 "port_2": "35511"
        #             }
        #         ]
        #     },
        #     "current_status": {
        #         "status": "waiting",
        #         "score": "False",
        #         "description": "waiting"
        #     }
        # }
    
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


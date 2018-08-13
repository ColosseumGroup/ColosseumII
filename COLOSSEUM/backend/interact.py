import http.client
import urllib.parse
import requests
import json
from django.views.decorators.csrf import csrf_exempt

    
req_method = ['GET','POST','PUT']
game_server_url = 'http://139.224.114.52'
port = 8081
default_headers ={
    "Content-Type":"application/json"
}
game_server_connect = http.client.HTTPConnection(game_server_url,port)

#interact to connect with game server.
def InteractWithGameServer_old(dict_param = None, headers = {"content-type":"application/json"},append_url='/',req=req_method[0]):
    params = json.dumps(dict_param)
    url = game_server_url+':'+str(port)+append_url
    request = game_server_connect.request(method=req,url=url,body=params,headers=headers)
    print("ready for request")
    response = game_server_connect.getresponse()
    print("ready for response")
    result = str(response.read(),encoding = "utf8")
    print(result)
    return eval(result)

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


#trials
dict_param = {
    'gameID': 'tt1122',
    'game': 'dealer_renju',
    'NPC': 'starter',
    'rounds': '1000',
    'random_seed': 'False',
    'game_define': 'False',
    'players': [
        {'name_1': 'Alice'},
        {'name_2': 'Bob'}
    ]
}

# InteractWithGameServer(dict_param=dict_param, append_url='/api/play',req='POST')
print(InteractWithGameServer(dict_param=dict_param,append_url='/api/play',req='POST'))
# print(InteractWithGameServer())



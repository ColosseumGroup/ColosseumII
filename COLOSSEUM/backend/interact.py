import http.client
import urllib.parse
import json
    
req_method = ['GET','POST','PUT']
game_server_url = '139.224.114.52'
port = 8081
game_server_connect = http.client.HTTPConnection(game_server_url,port)
print(game_server_connect)

#interfact to connect with game server.
def InteractWithGameServer(dict_param = None, headers = {"content-type":"application/json"},append_url='/',req=req_method[0]):
    params = json.dumps(dict_param)
    url = game_server_url+':'+str(port)+append_url
    print(params)
    request = game_server_connect.request(method=req,url=url,body=params,headers=headers)
    response = game_server_connect.getresponse()
    result = str(response.read(),encoding = "utf8")
    print(result)
    return eval(result)


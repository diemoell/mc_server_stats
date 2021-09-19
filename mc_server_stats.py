#-*-coding:utf-8-*-
import json
import http.server
from json import decoder
import os
from pathlib import Path

global mid_list_name
global uuid_to_name_fine
global FileList
list_uuid=[]
list_name=[]
mid_dict={}
end_dict={}
top_name_dict_dead={}
#Set your server saves's stats files
p=Path("../rlc/world/stats")
#Set your server saves's usernamecache file
p_uuid_fine=Path("../rlc/usernamecache.json")
uuid_find=open(p_uuid_fine,'r',encoding='utf-8')
list_uuid_fine=uuid_find.read().encode("utf-8")
uuid_to_name_fine=json.loads(list_uuid_fine)

def stats_find(find):
    life=0
    global list_this
    list_this=[]
    for key in uuid_to_name_fine:
        Files=Path(str(p)+"/"+key+".json")
        a=open(Files,'r',encoding='utf-8')
        list=a.read()
        this=json.loads(list)
        try:
            list_this.append(this[find])
        except:
            list_this.append(0)
            life=life+1
            if(life==len(uuid_to_name_fine)):
                return(404)
        try:
            top_name_dict_dead.update({uuid_to_name_fine[key]:this[find]})
        except:
            top_name_dict_dead.update({uuid_to_name_fine[key]:0})
    end=dict(sorted(top_name_dict_dead.items(),key=lambda x:x[1],reverse=True))
    a=0
    for i in end.items():
        end_dict.update({a:{i[0]:i[1]}})
        a=a+1
    return json.dumps(end_dict,ensure_ascii=False)

for key in uuid_to_name_fine:
    list_uuid.append(key)
    list_name.append(uuid_to_name_fine[key])

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(t):
        t.end_out=stats_find(str(t.path)[1:])
        if(t.end_out==404):
            t.send_response(404)
            return
        t.send_response(200)
        t.send_header("Content-Type","application/json")
        t.end_headers()
        t.wfile.write(t.end_out.encode('utf-8'))

if __name__== '__main__':
    serverAddress=('',7896)
    server=http.server.HTTPServer(serverAddress,RequestHandler)
    server.serve_forever()

#-*-coding:utf-8-*-
import json
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
p=Path("./stats")
out_p=Path("./list_dead.json")
p_uuid_fine=Path("usernamecache.json")
FileList=list(p.glob("*.json"))
uuid_find=open(p_uuid_fine,'r',encoding='utf-8')
list_uuid_fine=uuid_find.read().encode("utf-8")
uuid_to_name_fine=json.loads(list_uuid_fine)
def stats_find(find):
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
        try:
            top_name_dict_dead.update({uuid_to_name_fine[key]:this[find]})
        except:
            top_name_dict_dead.update({uuid_to_name_fine[key]:0})
    end=dict(sorted(top_name_dict_dead.items(),key=lambda x:x[1],reverse=True))
    a=0
    for i in end.items():
        end_dict.update({a:{i[0]:i[1]}})
        a=a+1
    return end_dict
for key in uuid_to_name_fine:
    list_uuid.append(key)
    list_name.append(uuid_to_name_fine[key])
end_deaths=stats_find("stat.sneakTime")
print(end_deaths)
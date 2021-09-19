#-*-coding:utf-8-*-
import json
from json import decoder
import os
import time
from pathlib import Path
list_uuid=[]
list_name=[]
list_dead=[]
mid_dict={}
end_dict={}
top_name_dict_dead={}
p=Path("../rlc/world/stats")
out_p=Path("../apa/webapps/dow/list_dead.json")
p_uuid_fine=Path("../rlc/usernamecache.json")
FileList=list(p.glob("*.json"))
uuid_find=open(p_uuid_fine,'r',encoding='utf-8')
list_uuid_fine=uuid_find.read().encode("utf-8")
uuid_to_name_fine=json.loads(list_uuid_fine)
for File in FileList:
    a=open(File,'r',encoding='utf-8')
    list=a.read()
    d=json.loads(list)
    try:
        dead=d['stat.deaths']
    except:
        print(File," is no dead")
        continue
    try:
        if (uuid_to_name_fine[str(File)[19:-5]]):
            name=uuid_to_name_fine[str(File)[19:-5]]
            list_uuid.append(str(File)[19:-5])
            list_name.append(name)
            list_dead.append(dead)
    except:
        continue
    top_name_dict_dead.update({name:dead})
    mid_list_name=list_name
list_dead=sorted(list_dead,reverse=True)
for find_un in range(0,len(list_dead)):
    for find_name in mid_list_name:
        if list_dead[find_un]==top_name_dict_dead.get(find_name):
            end_dict.update({find_un:{find_name:list_dead[find_un]}})
            mid_list_name.remove(find_name)
            break
end=json.dumps(end_dict,ensure_ascii=False)
out_file=open(out_p,'w',encoding='utf-8')
out_file.write(end)

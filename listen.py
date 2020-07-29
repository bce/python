# -*- coding: utf8 -*-
import json
import requests
headers = {'Content-Type': 'application/json'}
datas = json.dumps({"A": "1", "B": "2"})

import matplotlib.pyplot as plt
fig,ax=plt.subplots()
y1=[]
for i in range(50):
    r = requests.post("http://192.144.143.56:10081/easyrecord/sso/getCurrThreadCountMap", data=datas, headers=headers)
    data_dic = json.loads(r.text)
    a10001 = data_dic['data']['A10001']
    a10002 = data_dic['data']['A10002']
    a10003 = data_dic['data']['A10003']
    a10004 = data_dic['data']['A10004']
    a10005 = data_dic['data']['A10005']
    a10006 = data_dic['data']['A10006']
    y1 = a10006
    ax.cla()
    ax.bar(y1,label='test',height=y1,width=0.2)
    ax.legend()
    plt.pause(0.5)

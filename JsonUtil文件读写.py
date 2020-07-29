#!转成JSON格式
#-*- coding: UTF-8 -*-
import json
import io
import os
import re
import random
import codecs
import time

filepath=u"C:\\a\\"
for filename in os.listdir(filepath):
    print(filename)
    fr=io.open(unicode((filepath+filename).encode("utf-8"),"utf8"),'r', encoding ='UTF-8')
    content=fr.readlines()
    contentLines=''
    flag = False
    lastLineSign=""
    lastSign = ""
    keys=[]
    dict = {}
    for line in content:
        line=line.strip()
        if len(line)==0:
            continue
        contentLines = contentLines + line+"\",\""

    mat = re.findall(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2})",contentLines)
    for item in mat:
        mystr = ''.join(random.sample(['0','1','2','3','4','5','6','7','8','9','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'],32))
        keys.append(str(mystr))
        dict[str(mystr)] = item
        contentLines = contentLines.replace(item, str(mystr))
    contentLines = contentLines.replace(":","\":\"")
    for key in keys:
        contentLines = contentLines.replace(key, dict[key])
    contentLines = contentLines.replace("{\",\"","{\"")
    contentLines = contentLines.replace("\" [{","[{")
    contentLines = contentLines.replace(",\"}","}")
    contentLines = contentLines.replace("\"\"}\"","\"\"}")
    contentLines = contentLines.replace("\" {","{")
    contentLines = contentLines.replace("}]\"","}]")
    contentLines = contentLines.replace("}\",\"","}")

    fr.close()
    print(contentLines)
    try:
        fobj = codecs.open(filename,'a+','utf-8')
    except:
        print("*** file open error")
    else:
        #display the contents of the file to the screen.
        fobj.write(contentLines)
        fobj.flush()
        fobj.close()



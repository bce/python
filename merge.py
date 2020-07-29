#!合并文件
#-*- coding: UTF-8 -*-
import io
import os
import random
import codecs
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')
filepath=u"C:\\Chudequan\\tools\\python\\DML\\"
outfile = u"C:\\Chudequan\\tools\\python\\sl_dev.sql"
for filename in os.listdir(filepath):
    print(filename)
    fr=io.open(unicode((filepath+filename).encode("utf-8"),"utf8"),'r', encoding ='UTF-8')# 打开列表中的文件,读取文件内容
    try:
        newfile = codecs.open(outfile,'a+','UTF-8')
    except:
        print("*** file open error")
    else:
        #display the contents of the file to the screen.
        newfile.write(str(fr.read()))# 写入新建的文件中
        newfile.flush()
        newfile.close()
    fr.close() 

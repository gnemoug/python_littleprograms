#!/usr/bin/python
#-*-coding:utf8-*-
import time

fileHandle = open('a.txt','w')
for i in range(1,100000):
    fileHandle.write(''.join([str(i),"\n"]))
    time.sleep(1)#睡眠一秒钟
    fileHandle.flush()#刷新输出缓冲
    
fileHandle.close()

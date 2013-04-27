#!/usr/bin/python
#-*-coding:utf8-*-

import os,shutil,string

dir = '/home/guomeng/test'    #这里如果是windows系统，请按windows的目录形式写，如c:\\text
for i in os.listdir(dir):
    newfile = i.replace('.','_')    #用_替代.，规则可以自己写。
    oldname = dir +'/'+str(i)
    newname = dir +'/'+str(newfile)
    shutil.move(oldname,newname)     #shutil的用法在上篇日志中有描述。
    
print 'Rename finished!'  #注意此处“‘”应为英文版本否则极易出错

#shutil.move
#Recursively move a file or directory (src) to another location (dst).
#If the destination is a directory or a symlink to a directory, then src is moved inside that directory.
#The destination directory must not already exist. If the destination already exists but is not a directory, it may be overwritten depending on os.rename() semantics.
#If the destination is on the current filesystem, then os.rename() is used. Otherwise, src is copied (using copy2()) to dst and then removed.

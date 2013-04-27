#!/usr/bin/python
#-*-coding:utf8-*-

import os, string, sys, time, re, math, fileinput, glob, shutil

print os.listdir('/home/guomeng/test')

for file in os.listdir('/home/guomeng/test'):
    print os.path.splitext(file)
    if os.path.splitext(file)[1] == ".py":   #os.path.splitex返回一个文件名和后缀名的元组
        print file
        shutil.copy(file, "/home/guomeng")
#此时若复制到的文件路径含有此文件则会报错
#os.path.splitex返回一个文件名和后缀名的元组,诸如：('b', '.py')


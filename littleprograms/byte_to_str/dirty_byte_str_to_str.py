#!/usr/bin/python
#-*- coding:utf-8 -*-

a = [[b'xxxx',b'zzzzz',0,2,3],
    [b'liangshaoluo124',b'200905070410001',1,24,59]]

for i in a:
    i[0] = i[0].replace('b','')
    i[1] = i[1].replace('b','')

print a

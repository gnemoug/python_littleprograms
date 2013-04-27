#!/usr/bin/python
#-*- coding:utf-8 -*-

from pprint import pprint

vbuf=open('./1.txt','r').read().split('\n\n')
result=zip(*[x.strip().split('\n') for x in vbuf])
pprint(result)

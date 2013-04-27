#!/usr/bin/python
#-*- coding:utf-8 -*-

def a():
    try:
        print "in try"
        return "yes"
    finally:
        print "in finally"

b = a()
print b

#运行结果为:
#in try
#in finally
#yes

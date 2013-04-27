#!/usr/bin/python
#-*- coding:utf-8 -*-

def wraper(fun,*args,**wargs):
    print "in wraper"
    def wrapped(*args,**wargs):
        print "in wraped"
        return fun(*args,**wargs)
    return wrapped

@wraper
def test(name = "guomeng"):
    print "i am " + name

################会解析到最后一个return 的 function###################

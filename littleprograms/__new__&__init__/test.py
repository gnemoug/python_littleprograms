#!/usr/bin/python
#-*-coding:utf8-*-

class B(object):
    def __new__(cls, *args, **kwargs):
        print "in B new"
        new_cls = super(B,cls).__new__(cls, *args, **kwargs)
        return new_cls
    def __init__(self):
        print "in B"

class A(object):
    def __new__(cls, *args, **kwargs):
        print args,kwargs
        print "in A new"
        new_cls = B()
        return new_cls

    def __init__(self,data):
        print data

a = A("fuck you")

#!/usr/bin/python
#-*- coding:utf-8 -*-

class A(object):
    def __init__(self):
        self._fuck()

class B(A):
    def __init__(self):
        A.__init__(self)
    
    def _fuck(self):
        print "msg"

a = B()

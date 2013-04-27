#!/usr/bin/python
#-*-coding:utf-8-*-

def f1():
    print 'f1'

def f2():
    print 'f2'

def f3():
    print 'f3'

print 'test eval start!'
for i in xrange(1,4):
    eval('f' + str(i))()

print 'test globals start'
obj_dict = globals()#built in functions
for i in xrange(1,4):
    obj_dict['f' + str(i)]()


#!/usr/bin/python
#-*-coding:utf8-*-
#绑定方法也能提升Python不少性能
import time

class A():
  def f(self, n):
    return n

a = A()

t1 = 0
f = a.f
for j in xrange(10):
  sum = 0
  t = time.time()
  for i in xrange(1000000):
    sum += f(i)
  t1 += time.time() - t

t2 = 0
for j in xrange(10):
  sum = 0
  t = time.time()
  for i in xrange(1000000):
    sum += a.f(i)
  t2 += time.time() - t

print t1 /10
print t2 /10
print (t2 - t1) / t2 * 100, '%'

#结果：

#0.85
#1.00780000687
#15.6578691994 % 

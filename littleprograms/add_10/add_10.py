#!/usr/bin/python
#-*-coding:utf8-*-

from itertools import combinations

def select_sub_list(alist):
    select_list = [j for i in xrange(len(alist)) for j in combinations(alist,i) if sum(j) == 10]
    return list(set(select_list))
#combinations('ABCD', 2)      >>>>  AB AC AD BC BD CD
print select_sub_list([1,2,4,3,5,8,10])

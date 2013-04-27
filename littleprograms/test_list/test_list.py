#!/usr/bin/python
#-*- coding:utf-8 -*-

from pprint import pprint

original = [
    ('lilei', 24), ('hanmeimei', 23), ('dajiangyou', 23),
    ('jiaoshou', 1), ('zhuanjia', 1), ('mcshitou', 26),
    ('danteng', 25), ('jiyou', 26), ('papapa', 20), ('jiji', 26),
]

#test
d = {}
for name, age in original:
    d.setdefault(age, []).append(name)
pprint(d)
e = sorted(d.items(), key=lambda item: (len(item[1]), item[0]))#test
pprint(e)
f = lambda name, age: (name[0] if len(name) == 1 else sorted(name), age)
output = [f(name, age) for age, name in e]
pprint(output)

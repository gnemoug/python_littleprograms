#!/usr/bin/python
#-*-coding:utf-8-*-

row = []
secondfile = open("2")

for i in secondfile.readlines():
    row.append(i)

secondfile = open("2")

for i in secondfile.readlines():
    firstfile = open("1")       #由于第一个循环读出来后就已经到文件尾了，所以应该在此处加上这行
    for j in firstfile.readlines():#但是对于list变量等可以循环读
        if not cmp(i,j):
            try:
                row.remove(i)
            except ValueError as err:
                print(err)

print(row)

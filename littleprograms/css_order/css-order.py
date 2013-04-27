#!/usr/bin/python
#-*- coding:utf-8 -*-

with open('test.css') as rf:
    begin = True
    temp = ''
    result = []
    for i in rf.read():
        if i in ('{','}',';','\n','/'):
            if i == '{':
                result.append(','.join([j.strip() for j in (temp + i).split(',')]))
                temp = ''
            elif i == '\n':
                continue
            elif i == ';':
                result.append(' '*4 + (temp + i).strip())
                temp = ''
            elif i == '}':
                result.append(i)
                temp = ''
            elif i == '/':
                if begin:
                    temp = '/'
                else:
                    result.append(temp + i)
                    temp = ''
                begin = not begin
        else:
            temp += i
    with open('result.css','w') as wf:
        wf.write('\n'.join(result)) 

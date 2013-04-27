#!/usr/bin/python
#-*-coding:utf8-*-

raw_str = raw_input("please input a string\n")
j = 0
char_list,int_list,last_char = [],[],[]
for i in raw_str:
    if i == ' ':
        int_list.append(j)
        j = 0
    else:
        char_list.append(i)
        j+=1
int_list.append(j)
char_list.sort()
for i in int_list:
    for j in range(0,i):
        last_char.append(char_list.pop(0)) 
    last_char.append(' ')
print ''.join(last_char)

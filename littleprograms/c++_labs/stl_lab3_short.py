#!/usr/bin/python
#-*-coding:utf8-*-

raw_str  = raw_input ( "please input a string\n" )
tmp_str = filter(lambda c:not c.isspace() ,sorted(raw_str,reverse=True))
new_str = ''.join( chr if chr.isspace() else tmp_str.pop() for chr in raw_str )

print new_str

#当要由一个列表生成新列表时，考虑用filter()函数和列表综合

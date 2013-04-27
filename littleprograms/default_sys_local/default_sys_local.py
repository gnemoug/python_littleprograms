# coding:utf-8
 
import sys
import locale
 
def p(f):
    print '%s.%s(): %s' % (f.__module__, f.__name__, f())
 
#返回当前系统默认使用的字符集
p(sys.getdefaultencoding)
 
#系统默认使用的将字符集存到文件的编码格式
p(sys.getfilesystemencoding)
 
#获取默认的区域设置并返回tuple(语言, 编码)
p(locale.getdefaultlocale)
 
#Return the encoding used for text data, according to user preferences.  
p(locale.getpreferredencoding)

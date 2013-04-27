#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
    Created on 2011-11-19
     
    @author: icejoywoo
    这个实现了一个简单的original server,我会借助这个source，分析http协议或者说http运作过程
'''
import socket
import datetime
############################bind programe to a port#################################
"""
    这里是将程序绑定到特定的port，并监听
"""

# 初始化socket
s = socket.socket()
# 获取主机名, 也可以使用localhost
#host = socket.gethostname()
host = "localhost"
# 默认的http协议端口号
port = 9999
 
# 绑定服务器socket的ip和端口号
s.bind((host, port))

# 服务器名字/版本号
server_name = "MyServerDemo/0.1"
 
# 缓存时间, 缓存一天
expires = datetime.timedelta(days=1)
# GMT时间格式
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
# 相应网页的内容
content = '''
<html>
<head><title>MyServerDemo/0.1</title></head>
<body>
<h1>Hello, World!</h1>
</body>
</html>
'''
 
# 可同时连接五个客户端
s.listen(5)
############################bind programe to a port#################################
# 提示信息
print "You can see a HelloWorld from this server in ur browser, type in", host, "\r\n"
 
# 服务器循环
while True:
    # 等待客户端连接
    c, addr = s.accept()
    print "Got connection from", addr, "\r\n"
     
    # 显示请求信息
    print "--Request Header:"
    # 接收浏览器的请求, 不作处理
    data = c.recv(1024)
    print data
############################根据http1.0协议构建http协议包内容#################################
    # 获得请求的时间
    now = datetime.datetime.utcnow()
 
    # 相应头文件和内容,注意这里不能格式话，意思就是不能将这些str向前移,因为会破坏数据包格式，会将空格也发送出去。eg:
#    response = '''HTTP/1.1 200 OK
#        Server: %s
#        Date: %s
        
    response = '''HTTP/1.0 200 OK
Server: %s
Date: %s
Expires: %s
Content-Type: text/html;charset=utf8
Content-Length: %s
Connection: keep-alive

%s''' % (
server_name,
now.strftime(GMT_FORMAT),
(now + expires).strftime(GMT_FORMAT),
len(content),
content
)
    # 发送回应
############################根据http1.0协议构建http协议包内容#################################
    c.send(response)
    print "--Response:\r\n", response
    c.close()

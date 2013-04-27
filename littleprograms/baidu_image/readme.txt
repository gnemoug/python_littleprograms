使用说明:
在当前文件目录下创建文件夹baiduimg，然后运行程序即可


这次挑战一下高难度的抓图，从上文可以看出python的效率要比php好很多，抓取海量图片
目标：http://image.baidu.com 美女系列的图片
实现思路：参考：php和python 抓取百度美女图片代码
难点：百度图片美女系列 大概有100000+页*60 大概是600w+张。。。我勒个擦600w++
是个很大的挑战：
第一版程序：timeout
参考php和python 抓取百度美女图片代码 的代码改版
效果：在进入300页+的时候出现问题，timeout
升级办法：设置urllib超时
import socket
 socket.setdefaulttimeout(10)# 10 秒钟后超时
如果是urllib2库：
urllib2.urlopen('http://www.google.com', timeout=10)
第二版本程序:HTTP Error 404: Not Found
HTTP Error 404: Not Found
遇到很慢的图片资源了，解决办法，增加http code 判断
urlopen返回对象提供方法：
-         read() , readline() ,readlines() , fileno() , close() ：这些方法的使用方式与文件对象完全一样
-         info()：返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息
-         getcode()：返回Http状态码。如果是http请求，200请求成功完成;404网址未找到
-         geturl()：返回请求的url
第三版本程序IOError: [Errno socket error] timed out
到500页的时候，出现IOError: [Errno socket error] timed out
我勒个擦 IO读写不够了
解决办法：如果报错 直接跳出这个
try:
                    dataimg = urllib.urlopen(n['obj_url'])
                except IOError,e:
                    if e.message=="time out":
                        break
第四版本：socket.timeout: timed out
到600页的时候：
Traceback (most recent call last):
  File "/data/bookuu/web/work/shell/py/baiduimg.py", line 33, in <module>
    file_object.write(dataimg.read())
  File "/usr/local/lib/python2.7/socket.py", line 349, in read
    data = self._sock.recv(rbufsize)
socket.timeout: timed out
读写函数hold不住了，解决办法同第三本 增加对file函数异常判断
五版本：凡是涉及io的函数 都有可能报错
解决办法：全部增加try except 判断
得到后的新版的程序 目前没有报错:

程序说明：
引入类库 创建文件夹
循环体内：每600页自动打包压缩，并移除原文件图片
对每个设计io的函数增加异常判断
对图片格式继续判断，默认jpg
超出100000页后 自动打包压缩 退出程序

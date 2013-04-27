#!/usr/bin/python
#-*-coding:utf-8-*-

import urllib,json,socket
import random,os
import sys,datetime

starttime = datetime.datetime.now()
socket.setdefaulttimeout(10)
dir ='./baiduimg/'
if not os.path.isdir(dir):
	os.mkdir(dir)
i=1
j=1
p=60
while i<100000:

	if i%600==0:
		zipname = 'baiduzip_'+str(i)+'.zip'
		print 'make a zip file'
		os.system('zip -6qrm /data/bookuu/web/work/index/adunion/outdata/'+zipname+' /data/bookuu/web/work/index/adunion/outdata/baiduimg/*')
		print zipname+' file is ok!'
		#http://image.baidu.com/i?tn=listjson&word=liulan&oe=utf-8&ie=utf8&tag1=%E6%90%9E%E7%AC%91&tag2=%E5%85%A8%E9%83%A8&sorttype=0&pn=30&rn=60&requestType=1&1357639151100
	url ='http://image.baidu.com/i?tn=listjson&word=liulan&oe=utf-8&ie=utf8&tag1=%E6%91%84%E5%BD%B1&tag2=%E5%85%A8%E9%83%A8&sorttype=0&pn='+str(p*i)+'&rn=60&requestType=1&'+str(random.random())

	try:
		ipdata = urllib.urlopen(url).read()
	except IOError,e:
		#if e.message=="time out":
		print('img %s_%s is false1' % (i,j) )
		break
	else:
		ipdata1 = json.loads(ipdata)
		if ipdata1['data']:
			for n in ipdata1['data']:
				if n and n['obj_url']:
					try:
						dataimg = urllib.urlopen(n['obj_url']).read()
					except IOError,e:
						#if e.message=="time out":
						print('img %s_%s is false2' % (i,j) )
						break
					else:
						fPostfix = os.path.splitext(n['obj_url'])[1]
						if (fPostfix == '.png' or fPostfix == '.jpg' or fPostfix == '.PNG' or fPostfix == '.JPG'):
							filename = dir+os.path.basename(n['obj_url'])
						else:
							filename = dir+os.path.basename(n['obj_url'])+'.jpg'
						try:
							file_object = open(filename,'w')
							file_object.write(dataimg)
							file_object.close()
						except socket.timeout,e:
							#if e.message=="timed out":
							print('img %s_%s is false3' % (i,j) )
							break
						else:
							#urllib.urlretrieve(n['obj_url'],filename)
							print('img %s_%s is ok' % (i,j) )
							j +=1
		else:
			break
	i +=1
endtime = datetime.datetime.now()
print (endtime-starttime).seconds
os.system('zip -6qrm /data/bookuu/web/work/index/adunion/outdata/baiduimg_'+str(i)+'.zip /data/bookuu/web/work/index/adunion/outdata/baiduimg/*')
sys.exit()
			

#!/usr/bin/python
#-*-coding:utf-8-*-
#写在linux计划任务里定时执行，当有新用户登陆时候发送用户名到指定邮箱通知管理员。
from smtplib import SMTP
import subprocess

smtp = "smtp.qq.com"
user = '1849580896'
password = 'gnemoug309513;;'

run_comd = subprocess.Popen('w|grep pts',shell=True,stdout=subprocess.PIPE) #执行一个进程
data = run_comd.stdout.read()   #获取输出（stdout）文件对象的数据
mailb = ["服务器有新用户登录",data]
#print mailb
mailh = ["From: 1849580896@qq.com", "To: gnemoug@gmail.com", "Subject: 用户登录监控"]
mailmsg = "\r\n\r\n".join(["\r\n".join(mailh), "\r\n".join(mailb)]) #按照既定格式书写邮件内容

def send_mail():
    send = SMTP(smtp)   #与SMTP服务器之间的连接
    send.login(user,password)   #登录验证
    result = send.sendmail("1849580896@qq.com", ("gnemoug@gmail.com",), mailmsg)
    send.quit()
if data == '':
    pass
else:
    send_mail()


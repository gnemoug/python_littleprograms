#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    server.py:xml请求服务器
#    usage:  python server.py  or(chmod +x server.py;./server.py)
#        (fantasy <fantasy614@gmail.com>）
#           2010/11/17
#ChangeLog：
#    2010/11/17
#1.实现基本功能
#
#TODO:
#1.加入错误机制，目前程序当请求不正确时无结果放回
#2.绑定端口可从命令行传入
#
#BUG:
#

from BaseHTTPServer import HTTPServer ,BaseHTTPRequestHandler
from xml.dom.minidom import Document
import MySQLdb


class RequestHandler(BaseHTTPRequestHandler):
    conn = MySQLdb.connect (host = "172.29.142.41",user = "root",
                        passwd = "whpact",
                        db = "cybervision_new",
                        charset="utf8")
                        #use_unicode = False)
    cursor = conn.cursor() 

    def __del__(self): 
        pass

    def _writeheaders(self):
        self.send_response(200)
        self.send_header('Content-type','text/xml')
        self.end_headers()
    
    def do_HEAD(self):
        self._writeheaders()


    def getxml(self,date,type):
        dom = Document()
        ids = dom.createElement("ids")
        dom.appendChild(ids)
        sql = "SELECT change_time,type,max(id) FROM  xml where date(change_time) ='%s' and type='%s' group by change_time"%(date,type)
        
        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchall ()
            for row in rows:
                id = dom.createElement("id")
                id.setAttribute("changetime", str(row[0]))
                id.setAttribute("type", row[1])
                idText = dom.createTextNode(str(row[2]))
                id.appendChild(idText)
                ids.appendChild(id)
            xmltext = dom.toxml(encoding="utf-8")
            return self.wfile.write(xmltext)
        except:
            return

        
    def getid(self,id):
        sql = "SELECT xmlcontent FROM  xml where id=%s"%id
        #try:
        print sql
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        xmlcontent = row[0].encode("utf-8")#onicode(row[0],"utf8")   #print row
        return self.wfile.write(xmlcontent)
#        except:
#            return

    def parse_param(self,path):
        """parse params"""
        #print dir(self)
        #date=2010-9-1&type=botnet
        if path.startswith("id="):
            id=path.split("=")[-1]
            self.getid(id)
        elif path.startswith("date"):
            date = path.split("&")[0].split("=")[1]
            print date
            type= path.split("&")[1].split("=")[1]
            self.getxml(date,type)
            
        if path=="crossdomain.xml":
            crossdomain = open(path,'r')
            self.wfile.write(crossdomain.read())
            return

    def do_GET(self):
        """
        return xml to the client
        """
        self._writeheaders()
        path=self.path.strip('/')
        print path
        self.parse_param(path)

def main():
    serveraddr = ('127.0.0.1',8000)
    srvr = HTTPServer(serveraddr,RequestHandler)
    srvr.serve_forever()
if __name__ == "__main__":
    main()


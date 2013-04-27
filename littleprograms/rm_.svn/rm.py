#!/usr/bin/python
#-*-coding:utf-8-*-

import os
with open('svn_doc') as rf:
    for i in rf.readlines():
        os.system('rm -R %s'%i)

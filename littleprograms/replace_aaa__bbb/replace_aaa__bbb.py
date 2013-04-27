#!/usr/bin/python
#-*-coding:utf-8-*-
import os
import argparse

def replace_alldir(search_directory,oldstr,newstr):
    result_path_filename = list()
    result_path_filename.extend([os.path.join(dirpath,filename) for dirpath,dirnames,filenames in os.walk(search_directory) for filename in filenames])
    print result_path_filename

    for file in result_path_filename:
        file_result_content = ''
        with open(file) as rf:
            file_result_content = rf.read().replace(oldstr,newstr)
        with open(file,'w') as wf:
            wf.write(file_result_content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--rootdir',help='specific the root directory')
    parser.add_argument('oldstr',help='string to be replaced')
    parser.add_argument('newstr',help='string to replace')
    args = parser.parse_args()
    search_directory = args.rootdir
    if not search_directory:
        replace_alldir(os.path.dirname(os.path.abspath(__file__)),args.oldstr,args.newstr)
    else:
        replace_alldir(search_directory,args.oldstr,args.newstr)

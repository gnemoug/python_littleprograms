#!/usr/bin/python
#-*-coding:utf8-*-
import sys
import os
import argparse
import pdb
from pprint import pprint

def find_path_file(specific_dir,search_directory):
    """
    result_path_filename
    """
    print specific_dir
    result_path_filename = list()
    result_path_filename.extend([os.path.join(os.path.abspath(dirpath),dirname) for dirpath,dirnames,filenames in os.walk(search_directory) for dirname in dirnames if dirname == ('.' + specific_dir)])
    pprint(result_path_filename)

def save_result_to_file(_filename,specific_dir,search_directory):
    """
    save result to specific file
    """
    result_path_filename = list()
    result_path_filename.extend([os.path.join(os.path.abspath(dirpath),dirname) for dirpath,dirnames,filenames in os.walk(search_directory) for dirname in dirnames if dirname == ('.' + specific_dir)])
    with open(_filename,'w') as f:
        f.write("\n".join(result_path_filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_suffix",help="specific the file suffix")
    parser.add_argument("rootdir",help="specific the root directory")
    parser.add_argument("-f","--file",help="record result to file")
    args = parser.parse_args()
#os.path.dirname(os.path.abspath(__file__))..............程序当前路径
    specific_dir = args.file_suffix
    search_directory = args.rootdir
    if args.file:
        filename = args.file
        save_result_to_file(filename,specific_dir,search_directory)
    else:
#        find_file(specific_dir,search_directory)
        find_path_file(specific_dir,search_directory)

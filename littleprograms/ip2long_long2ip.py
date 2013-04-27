#!/usr/bin/python
# coding: utf-8
"""

    将点分十进制 IP 地址转换成无符号的长整数和将无符号长整形转换为点分十进制 IP 地址形式
"""
import socket
import struct
import sys

def ip2long (ip):
    "将点分十进制 IP 地址转换成无符号的长整数"

    return struct.unpack("!I", socket.inet_aton(ip))[0]

def long2ip (lint):
    "将无符号长整形转换为点分十进制 IP 地址形式"

    return socket.inet_ntoa(struct.pack("!I", lint))
    
def main():
    ipa = "172.29.142.135"
    ipa_int = ip2long(ipa)
    print ipa_int
    ipb = "172.29.142.136"
    ipb_int = ip2long(ipb)
    print ipb_int

if __name__ == '__main__':
    sys.exit(main())

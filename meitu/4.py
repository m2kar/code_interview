#!python3 
# 本程序为geoip.py
# 输入参数
# geoip.py <geo_ip_file_path> <ip_address>
# for Example:
# geoip.py geo_ipfile.txt 123.123.123.123.123

import sys
import ipaddress

def read_db(fname):
    db={}
    with open(fname) as fp:
        for line in fp:
            sip0,sip1,pos=line.strip().split(",")
            ip0=ipaddress.IPv4Address(sip0)
            ip1=ipaddress.IPv4Address(sip1)
            net=ipaddress.IPv4Address(ip0&ip1)
        
    return db

fname=sys.argv[1]
ip=sys.argv[2]
read_db(fname)
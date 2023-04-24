#filter,parse, and metric functions
def filter(fn):
    print('called filter function in filter_packets.py')
    read(fn)

def read(filename):
    mid_step = filename.split(".")
    nfile = mid_step[0] + "_filtered." + mid_step[1]
    
    unfnode = open(filename, "r")
    fnode = open(nfile, "w")
    fnode.close()
    fnode = open(nfile, "a")
    line = unfnode.readline()
    
    while line:
        if "unreachable" not in line:
            if "ICMP" in line:
                fnode.write(line)
        line = unfnode.readline()

    unfnode.close()
    fnode.close()

def parse(filename):
    parseList = []
    with open(filename) as f:
        content = f.readlines()
        for line in content:
            line = line.rstrip()
            line = line.split(",")
            parseList.append(line)
    return parseList


def main():
    parseList = (parse('debug.txt'))
    for packet in parseList:
        print(packet)
 #This is where we call the functions and ask for parameters
from filter_packets import *
from packet_parser import *
from compute_metrics import *

import sys

fileName = sys.argv[1]

L = []
ip = "192.168.100.1"

if( "1" in fileName):
    ip = "192.168.100.1"
elif( "2" in fileName):
    ip = "192.168.100.2"
elif( "3" in fileName):
    ip = "192.168.200.1"
elif( "4" in fileName):
    ip = "192.168.200.2"
elif( "5" in fileName):
    ip = "192.168.100.254"

filter(fileName)
parse(fileName)
compute(L, ip, fileName)
if __name__ == '__main__':
    main()


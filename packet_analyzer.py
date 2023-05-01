#filter,parse, and metric functions
#This is where we call the functions and ask for parameters
from filter_packets import *
from packet_parser import *
from compute_metrics import *
import sys

fileName = sys.argv[1]

ip = "192.168.100.1"

if "1" in fileName:
    ip = "192.168.100.1"
elif "2" in fileName:
    ip = "192.168.100.2"
elif "3" in fileName:
    ip = "192.168.200.1"
elif "4" in fileName:
    ip = "192.168.200.2"
elif "5" in fileName:
    ip = "192.168.100.254"

filtered = filter(fileName)
parseList = parse(filtered)
compute(parseList, ip, fileName) 

#filter,parse, and metric functions
def filter(fn):
    print('called filter function in filter_packets.py')
    return read(fn)

def read(file_name):
    mid_step = file_name.split(".")
    new_file_name = mid_step[0] + "_filtered." + mid_step[1]
    
    unfiltered_node = open(file_name, "r")
    filtered_node = open(new_file_name, "w")
    filtered_node.close()
    filtered_node = open(new_file_name, "a")
    line = unfiltered_node.readline()
    
    while line:
        if "unreachable" not in line:
            if "ICMP" in line:
                filtered_node.write(line)
        line = unfiltered_node.readline()

    unfiltered_node.close()
    filtered_node.close()
    return new_file_name

def parse(filename):
    print('called parse function in packet_parser.py')
    parseList = []
    with open(filename) as f:
        content = f.readlines()
        for line in content:
            line = line.rstrip()
            line = line.split(",")
            parseList.append(line)
    return parseList



 #This is where we call the functions and ask for parameters

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
# compute(parseList, ip, fileName) # compute function is not defined


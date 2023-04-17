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


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

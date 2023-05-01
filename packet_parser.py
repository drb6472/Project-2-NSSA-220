def parse(filename):
    print('called parse function in packet_parser.py')
    parseList = []
    with open(filename) as f:
        for line in f:
            parseList.append(line.rstrip().split())
    return parseList

# This is for hex but did not complete 
# def parse(filename):
    print('called parse function in packet_parser.py')
    parseList = []
    with open(filename, "rb") as f:
        content = f.readlines()
        for line in content:
            hex_values = []
            for byte in line:
                hex_value = hex(byte)[2:].zfill(2)  # Convert byte to hex string
                hex_values.append(hex_value)
            parseList.append(hex_values)
    return parseList

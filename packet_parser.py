def parse(filename):
    print('called parse function in packet_parser.py')
    parseList = []
    with open(filename) as f:
        content = f.readlines()
        for line in content:
            line = line.rstrip()
            line = line.split()
            parseList.append(line)
    return parseList

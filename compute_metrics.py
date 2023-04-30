def compute(parsedList, ip, filename):
    print('called compute function in compute_metrics.py')
    midstep = filename.split(".")
    newfilename= midstep[0] + "_filtered.txt"
    file = open(newfilename, "r")
    for line in file:
        parsedList.append(line.split())
    file.close()
    reqsent = 0
    reqrcvd = 0
    repsent = 0
    reprcvd = 0
    reqdatasent = 0
    reqdatarcvd = 0
    repbytessent = 0
    repbytesrcvd = 0
    for i in parsedList:
        if i[8] == "reply":
            if i[2] == ip:
                repsent = repsent + 1
            elif i[3] == ip:
                reprcvd = reprcvd + 1
        if i[8] == "request":
            if i[2] == ip:
                reqsent = reqsent + 1
                reqbytessent = reqbytessent + int(i[5])
                reqdatasent = reqdatasent + int(i[5]) - 42
            elif i[3] == ip:
                reqrcvd = reqrcvd + 1
                reqbytesrcvd = reqbytesrcvd + int(i[5])
                reqdatarcvd = reqdatarcvd + int(i[5]) - 42
 
    outputName = "output.csv"
    with open(outputName, "a") as output:
        output.write(newfilename)
        output.write("  \n")
        output.write("Echo Requests Sent" + "," + "Echo Requests Received" + "," + "Echo Replies Sent" + "," + "Echo Replies Received\n")
        output.write(str(reqsent/2) + "," + str(reqrcvd/2) + "," + str(repsent/2) + "," + str(reprcvd/2) + "\n")
        output.write("Echo Request Bytes sent (bytes)" + "," + "Echo Request Data Sent (bytes)\n")
        output.write(str(reqbytessent/2) + "," + str(reqdatasent/2) + "\n")
        output.write("Echo Request Bytes Received (bytes)" + "," + "Echo Request Data Received (bytes)\n")
        output.write(str(reqbytesrcvd/2) + "," + str(reqdatarcvd/2) + "\n")
        output.write(" \n")

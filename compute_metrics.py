def compute(parsedList, ip, filename):
    print('called compute function in compute_metrics.py')
    midstep = filename.split(".")
    newfilename= midstep[0] + "_filtered.txt"
    file = open(newfilename, "r")
    for line in file:
        parsedList.append(line.split())
    file.close()
    # defining variables to be used
    reqsent = 0
    reqrcvd = 0
    repsent = 0
    reprcvd = 0
    reqdatasent = 0
    reqdatarcvd = 0
    reqbytessent = 0
    reqbytesrcvd = 0
    total = 0
    rttCount = 0
    avgdelayreply = 0
    delaycount = 0
    hop = 0
    requestcount = 0

    # data size metrics
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

    # time based metrics 
    for i in range(0, len(parsedList), 2):
        if parsedList[i][2] == ip and parsedList[i][8] == "request":
            total += (float(parsedList[i+1][1]) - float(parsedList[i][1]))
            rttCount += 1
        if parsedList[i][3] == ip and parsedList[i][8] == "request":
            avgdelayreply += float(parsedList[i+1][1]) - float(parsedList[i][1])
            delaycount += 1
    rttTotal = 1000 * (total / rttCount)
    echoreqthroughput = reqbytessent/total/1000
    echoreqgoodput = reqdatasent/total/1000
    avgdelayreply = ((avgdelayreply/delaycount) * 1000000)

    # distance based metric 
    for i in parsedList:
        if i[8] == "request":
            if "126" in i[11]:
                hop += 1
            else:
                hop += 3
        requestcount += 1
    hop = float(hop) / float(requestcount)

    # writing output to file
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
        output.write("Average RTT (miliseconds)" + "," + str(rttTotal) + "\n")
        output.write("Echo Request Throughput (kB/sec)" + "," + str(echoreqthroughput) + "\n")
        output.write("Echo Request Goodput (kB/sec)" + "," + str(echoreqgoodput) + "\n")
        output.write("Average Reply Delay" + "," + str(avgdelayreply) + "\n")
        output.write("Average Echo Request Hop Count" + "," + str(hop) + "\n")
        output.write(" \n")

fileLines = open("lines.txt", "r")
line = fileLines.readlines()
fileLines.close()
maxJ = 0
for i in line:
    splitLine = i.split()
    for j in range(len(splitLine)):
        count = (len(splitLine[j]))
        if count >= maxJ:
            maxJ = count
fileLinesResult = open("lines_result.txt", "w")
for x in line:
    if len(x.replace("\n", "")) == maxJ:
        fileLinesResult.write(x)

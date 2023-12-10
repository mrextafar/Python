fileLine = open("line.txt", "r")
line = fileLine.readlines()
s = ""
for i in line[::-1]:
    for j in i.split():
        s = s + j
        print(j)
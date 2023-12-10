fileNumber = open("numbers.txt", "r")
numbers = fileNumber.read().split()
fileNumber.close()
last = 1
dig = 0
for i in numbers:
    if i.isdigit():
        dig += 1
        last = last * int(i)
result = last ** (1/dig)
fileResults = open("results.txt", "w")
fileResults.write(str(result))
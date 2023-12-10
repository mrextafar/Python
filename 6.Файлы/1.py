fileNumber = open("numbers.txt", "r")
numbers = fileNumber.read().split()
fileNumber.close()
last = 0
for i in numbers:
    last = last + int(i)
fileResults = open("results.txt", "w")
result = last/len(numbers)
fileResults.write(str(result))
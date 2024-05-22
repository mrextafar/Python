countEu = 0
countMin = 0
countRec = 0
def GCDEuclid(num1,num2):#O(log(N))
    global countEu
    while num1 != 0 and num2 != 0:
        countEu += 1
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1+num2

def GCDMinus(num1,num2):#O(N)
    global countMin
    while num1 != num2:
        countMin += 1
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1

def GCDRecursive(num1, num2):#O(log(N))
    global countRec
    countRec += 1
    if (num2 == 0):
        return num1
    else:
        return GCDRecursive(num2, num1 % num2)

print(GCDEuclid(30,18), countEu)
print(GCDMinus(30,18), countMin)
print(GCDRecursive(30,18), countRec)

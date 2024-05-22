count = 0
def PrimeNumbers(_range):#O(N^2)
    global count
    res = [i for i in range(_range+1)]
    i = 2
    while i <= _range:
        if res[i] != 0:
            j = i+i
            while j <= _range:
                res[j] = 0
                j = j + i
                count+=1
        i += 1
    res = [i for i in res if i != 0]
    return res
print(PrimeNumbers(300))
print(count)
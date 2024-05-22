count = 0
def Exponentiation(num, degree):#O(N)
    global count
    count += 1
    if degree == 0:
        return 1
    return Exponentiation(num, degree-1)*num

print(Exponentiation(2,99))
print(count)
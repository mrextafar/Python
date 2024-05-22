count = 0
def Factorial(n):
    global count
    res = 1
    for i in range(1, n + 1):
        count += 1
        res *= i
    return res

def FactorialRec(n):
    global count
    if n == 0:
        return 1
    else:
        count += 1
        return n * FactorialRec(n - 1)
num = 100
print(Factorial(num)) # O(N)
print(count)
count = 0
print(FactorialRec(num)) # O(N)
print(count)
count = 0
def FibonacciRec(n):#O(2^N)
    global count
    count += 1
    if n in (1, 2):
        return 1
    return FibonacciRec(n - 1) + FibonacciRec(n - 2)

def FibonnaciCycle(n):#O(N)
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2

n = 4
print(FibonacciRec(n))
print(FibonnaciCycle(n))
print(count)

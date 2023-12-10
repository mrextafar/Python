numbers = list(map(int, input().split()))
arif = sum(numbers)/len(numbers)
for y in numbers:
    if arif < y:
        print(y)
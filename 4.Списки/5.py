numbers = list(map(int, input().split()))
xMax = numbers[0]

for x in numbers:
    if x > xMax:
        xMax = x
        print(x)
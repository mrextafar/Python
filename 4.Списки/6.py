numbers = list(map(int, input().split()))
maxDia = int(input())
minDia = int(input())

for x in numbers:
    if x >= minDia and x <= maxDia:
        print(numbers.index(x))
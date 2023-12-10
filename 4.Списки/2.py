numbers = list(map(int, input().split()))
numbersM = []
for x in numbers:
    x = x ** 2
    numbersM.append(x)
print(numbersM)

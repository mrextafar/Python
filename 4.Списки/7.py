numbers = list(map(int, input().split()))
s = bool
for x in numbers:
    if numbers.count(x) > 1:
        s = 1
if s == 1:
    print("Есть повторяющиеся")
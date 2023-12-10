numbers = list(map(int, input().split()))
numbers.sort(key = abs)
print(numbers[::-1])
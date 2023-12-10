numbers = list(map(int, input().split()))
numbers_set = set(numbers)
max_number = 0
result = 0
for item in numbers_set:
    if numbers.count(item) > max_number:
        max_number = numbers.count(item)
        result = item
print(result)
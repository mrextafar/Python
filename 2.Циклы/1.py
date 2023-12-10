number = int(input())
maxNum = 0

for num in str(number):
    if num.isdigit() and int(num) > maxNum:
        maxNum = int(num)

print(maxNum)
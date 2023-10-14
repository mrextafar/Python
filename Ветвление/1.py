print("Вас приветсвтует программа которая находит наибольшее число из 3-х введёных чисел")
print("Введите первое число")
first = int(input())
print("Введите втолрое число")
second = int(input())
print("Введите третье число")
third = int(input())

num = [first, second, third]
num.sort()
maxNum = num[2]

print(str(maxNum) + " наибольшее число")


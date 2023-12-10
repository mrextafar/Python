print("Вас приветсвует программа которая определяет наименьшее число из 4-х введённых чисел")
print("Введите первое число")
number1 = int(input())
print("Введите второе число")
number2 = int(input())
print("Введите третье число")
number3 = int(input())
print("Введите четвёртое число")
number4 = int(input())

numbers = [number1, number2, number3, number4]
numbers.sort()

print("Наименьшее число " + str(numbers[0]))
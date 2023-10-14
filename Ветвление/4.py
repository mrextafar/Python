import calendar
print("Вас приветсвтует программа которая определяет количество дней в месяце по введённому номеру месяцу и году")
print("Введите номер года")
year = int(input())
print("Введите номер месяца")
month = int(input())

lastDay = calendar.monthrange(year, month)

print("В указаном месяце " + str(lastDay[-1]) + " день")
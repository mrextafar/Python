print("Вас приветствует программа которая пишет фразу 'Мы нашли в лесу K грибов', причем согласовывает окончание слова 'гриб' с числом K")
print("Введите количество грибов")
number = int(input())

#print(*f'{number}')
num = [*f'{number}']
lastNumber = num.index[-1]
if lastNumber in [1]:
    print("Гриб")
elif lastNumber in [234]:
    print("Гриба")
elif lastNumber in [4567890]:
    print("Грибов")





#пока хз
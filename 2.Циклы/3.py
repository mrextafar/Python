number = int(input())
fact = 1

if number % 2 == 0:
    for num in range(2, number + 1, 2):
        fact = fact * num
    print (fact)
elif number % 2 != 0:
    for num in range(1, number + 1, 2):
        fact = fact * num
    print(fact)
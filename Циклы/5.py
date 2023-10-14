number = int(input())
even = 0
notEven = 0

for num in str(number):
    if int(num) % 2 == 0:
        even += 1
    else:
        notEven += 1
print(str(even) + " " + str(notEven))


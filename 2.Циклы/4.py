number = int(input())
otvetPlus = 0
otvetMnoj = 1

for num in str(number):
    otvetPlus = int(num)+otvetPlus
    otvetMnoj = int(num)*otvetMnoj

print(otvetPlus)
print(otvetMnoj)
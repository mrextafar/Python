number = str(input())
otvet = ""

for x in range(len(number)-1,-1,-1):
    otvet += number[x]

print(otvet)


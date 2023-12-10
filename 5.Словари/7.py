n = int(input())
dictionary = {}
while n != 0:
    n -= 1
    pokupka = list(input().split())
    print(pokupka)
    if pokupka[0] in dictionary:
        if pokupka[1] in dictionary:
            x = pokupka[2]
            c = int(y) + int(x)
            print(c)
            dictionary[pokupka[1]] = c
        else:
            dictionary[pokupka[1]] = pokupka[2]
        y = pokupka[2]
    else:
        if pokupka[1] in dictionary:
            x = pokupka[2]
            c = int(y) + int(x)
            print(c)
            dictionary[pokupka[1]] = c
        else:
            dictionary[pokupka[1]] = pokupka[2]
        y = pokupka[2]
print(pokupka[0], dictionary)
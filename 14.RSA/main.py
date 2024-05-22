def GCD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return(a+b)

def PrimeNumbers(_range):
    res = [i for i in range(_range+1)]
    i = 2
    while i <= _range:
        if res[i] != 0:
            j = i+i
            while j <= _range:
                res[j] = 0
                j = j + i
        i += 1
    res = [i for i in res if i != 0]
    return res

def SetPQ():
    pSelect = PrimeNumbers(100)
    for i in pSelect[:]:
        if i < 34:
            pSelect.remove(i)

    print(pSelect)
    p = int(input("Выберите первое число: "))
    
    while (p in pSelect) == False: 
        print(pSelect)
        p = int(input("Выберите другое первое число: "))
    pSelect.remove(p)
    print(pSelect)
    q = int(input("Выберите второе число: "))
    while (q in pSelect) == False:
        print(pSelect)
        q = int(input("Выберите другое второе число: "))
    print(f"p = {p}\nq = {q}")
    return p, q

def GetNFi(p, q):
    n = p * q
    fi = (p-1) * (q-1)
    return [n, fi]

def SetE(fi):
    eSelect = []
    for i in range(2, fi):
        if GCD(i, fi) == 1:
            eSelect.append(i)
    e = int(input(f"Выберите одно из этих чисел {eSelect}: "))
    while (e in eSelect) == False:
        e = int(input(f"Выберите одно из этих чисел {eSelect}: "))
    return e

def SetD(a, fi, e):
    dSelect = []
    for i in range(a**2):
        if (i * e) % fi == 1:
            dSelect.append(i)
    d = int(input(f"Выберите одно из этих чисел {dSelect}: "))
    while (d in dSelect) == False:
        d = int(input(f"Выберите одно из этих чисел {dSelect}: "))
    return d

def SetAndGetKeys():
    p, q = SetPQ()
    n, fi= GetNFi(p, q)
    e = SetE(fi)

    if p > q:
        a = p
    else:
        a = q

    d = SetD(a, fi, e)

    print(f"Открытый ключ: {e,n}")
    print(f"Закрытый ключ: {d,n}")
    return [e, d, n]

def Encryption(text, openKey):
    _text = text
    _key = openKey
    asciiText = [ord(char) for char in _text]

    cipher = []
    for i in asciiText:
        cipher.append((i**_key[0]) % _key[2])

    res = ""
    for i in range(len(cipher)):
        res = res + str(cipher[i]) + ' '
    return res

def Decryption(cipher, closedKey):
    _cipher = cipher
    _key = closedKey

    decipher = []
    for i in _cipher:
        decipher.append((int(i)**_key[1]) % _key[2])
    res = ''.join(chr(num) for num in decipher)
    return res

def WriteResultFile(result):
    with open("Result.txt", "w") as file:
        file.write(result)



answer = input("Вы хотите зашифровать(1) или расшифровать(2)?: ")
if answer == "1":
    answer = input("Вы хотите работать из файла? Да(1), Нет(2): ")
    if answer == "1":
        with open("Preset.txt", "r") as file:
            keys = list(map(int, file.readline().split()))
            text = file.readline()
        result = Encryption(text, keys)
        WriteResultFile(result)
        print(f"Ваш шифр: {result}")
    elif answer == "2":
        text = input("Ваш текст: ")
        result = Encryption(text, SetAndGetKeys())
        WriteResultFile(result)
        print(f"Ваш шифр: {result}")
elif answer == "2":
    answer = input("Вы хотите работать из файла? Да(1), Нет(2): ")
    if answer == "1":
        with open("Preset.txt", "r") as file:
            keys = list(map(int, file.readline().split()))
            cipher = file.readline().split()
        result = Decryption(cipher, keys)
        WriteResultFile(result)
        print(f"Ваш шифр: {result}")
    elif answer == "2":
        cipher = input("Ваш шифр: ").split()
        result = Decryption(cipher, SetAndGetKeys())
        print(f"Ваша расшифровка: {result}")

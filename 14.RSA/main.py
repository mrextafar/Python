def GCD(a: int, b: int) -> int:
    'Считает Наибольший Общий Делитель'

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return(a+b)

def PrimeNumbers(value: int) -> list:
    'Решето Эратосфена'

    res = [i for i in range(value+1)]
    i = 2
    while i <= value:
        if res[i] != 0:
            j = i+i
            while j <= value:
                res[j] = 0
                j = j + i
        i += 1
    res = [i for i in res if i != 0]
    return res

def SetPQ() -> list:
    'Указываем p и q'

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

    return [p, q]

def GetNFi(p: int, q: int) -> list:
    'Высчитываем n(часть открытого и закрытого ключа) и fi(Функцию Эйлера)'

    n = p * q
    fi = (p-1) * (q-1)

    return [n, fi]

def SetE(fi: int) -> int:
    'Даём выбрать e(часть открытого ключа)'
 
    eSelect = []
    for i in range(2, fi):
        if GCD(i, fi) == 1:
            eSelect.append(i)
    e = int(input(f"Выберите одно из этих чисел {eSelect}: "))
    while (e in eSelect) == False:
        e = int(input(f"Выберите одно из этих чисел {eSelect}: "))

    return e

def SetD(a: int, fi: int, e: int) -> int:
    'Даём выбрать d(часть закрытого ключа)'

    dSelect = []
    for i in range(a**2):
        if (i * e) % fi == 1:
            dSelect.append(i)
    d = int(input(f"Выберите одно из этих чисел {dSelect}: "))
    while (d in dSelect) == False:
        d = int(input(f"Выберите одно из этих чисел {dSelect}: "))
    return d

def SetAndGetKeys() -> list:
    'Создаём и получаем открытый и закрытый ключ (нулевой и второй элементы это открытый ключ, первый и второй элементы это закрытый ключ)'

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

def Encryption(text: str, openKey: list) -> str:
    'Шифуем текст по открытому ключу'

    _key = openKey
    asciiText = [ord(char) for char in text]

    cipher = []
    for i in asciiText:
        cipher.append((i**_key[0]) % _key[2])

    res = ""
    for i in range(len(cipher)):
        res = res + str(cipher[i]) + ' '

    return res

def Decryption(cipher: str, closedKey: list) -> str:
    'Дешифруем по закрытому ключу'

    _key = closedKey
    decipher = []
    for i in cipher:
        decipher.append((int(i)**_key[1]) % _key[2])
    res = ''.join(chr(num) for num in decipher)

    return res

def WriteResultFile(result: str):
    'Записываем в файл'

    with open("Result.txt", "w") as file:
        file.write(result)

def MakingAnEncription():
    'Запуск шифрования'

    answer = input("Вы хотите работать из файла? Да(1), Нет(2): ")
    if answer == "1":
        with open("Preset.txt", "r") as file:
            keys = list(map(int, file.readline().split()))
            text = file.readline()
        result = Encryption(text, keys)

    elif answer == "2":
        text = input("Ваш текст: ")
        result = Encryption(text, SetAndGetKeys())

    WriteResultFile(result)
    print(f"Ваш шифр: {result}")

def MakingADecryption():
    'Запуск расшифрования'

    answer = input("Вы хотите работать из файла? Да(1), Нет(2): ")
    if answer == "1":
        with open("Preset.txt", "r") as file:
            keys = list(map(int, file.readline().split()))
            cipher = file.readline().split()
            for i in cipher:
                if i.isalpha():
                    raise Exception("Шифр не может быть словом")
        result = Decryption(cipher, keys)
        
    elif answer == "2":
        cipher = input("Ваш шифр: ").split()
        for i in cipher:
                if i.isalpha():
                    raise Exception("Шифр не может быть словом")
        result = Decryption(cipher, SetAndGetKeys())

    WriteResultFile(result)
    print(f"Ваш шифр: {result}")



answer = input("Вы хотите зашифровать(1) или расшифровать(2)?: ")
if answer == "1":
    MakingAnEncription()
elif answer == "2":
    MakingADecryption()

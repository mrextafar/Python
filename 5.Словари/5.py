dict_res = {"Волкобой": 2, "Пила-струна": 1, "Пылесос": 6, "Вентелятор": 6, "Цепь-арго": 3, "Сверло": 3, "Бур": 4, "Выживалово": 100, "Граната": 2}
listS = sorted(dict_res.items(), key=lambda item: item[1], reverse=True)
dict_sorted = {}
ves = 10
print(dict_res)
for i in range(len(listS)):
    x = listS[i][0]
    y = listS[i][1]
    dict_sorted[x] = y
print(dict_sorted)

for a in dict_sorted:
    if dict_sorted[a] <= ves:
        ves -= dict_sorted[a]
        print(a)
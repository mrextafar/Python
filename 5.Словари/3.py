words = input()
dict_res = {}
for x in words:
    y = words.count(x)
    dict_res[x] = y
print(dict_res)
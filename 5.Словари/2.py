keys = [1,2,3,4,5,6,7,8,9,10]
num = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"]
dict_res = dict()
for i in range(len(keys)):
    dict_res[keys[i]] = num[i]
print(dict_res)
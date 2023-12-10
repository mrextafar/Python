def bank(a, y):
    res = a + a * 0.1
    while y - 1 > 0:
        res = res + res * 0.1
        y -= 1
    return res
print(bank(10, 2))
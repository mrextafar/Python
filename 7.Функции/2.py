def mySum (_x, _y):
    res = sum(range(_x,_y)) + _y
    return res
x = int(input())
y = int(input())
c = 0
if x > y:
    c = y
    y = x
    x = c
print(mySum(x,y))
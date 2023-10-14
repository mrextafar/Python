min = int(input())
max = int(input())
step = float(input())
d = int((max - min)/step)

for x in range(d + 1):
    print("x= ", min, end = ' ')
    y = -0.23*min*min+min
    print("y= ", y)
    min = min + step
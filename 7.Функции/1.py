def average(*args):
    aver = sum(args[0]/len(args[0]))
    res = min(args[0], key=lambda num: abs(num - aver))
    return res
print(average(tuple(map(float, input().split()))))
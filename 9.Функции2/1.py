def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

def GCD(_arg):
    _arg.sort()
    while True:
        a = _arg[-1]
        b = _arg[-2]
        c = -1
        _arg.pop()
        _arg.pop()
        while c != 0:
            c = a - b * int(a/b)
            a = b
            b = c
            #print(a)
        for i in _arg:
            if i % a == 0:
                return a
            else:
                return 1


print(str(GCD([3315,120,20])) + " res")

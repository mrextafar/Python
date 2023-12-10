def date(d, m, y):
    vYear = tuple([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    neVYear = tuple([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    if m in range(1,13):
        if y % 100 == 0 and y % 400 == 0:
            if d <= vYear[m-1]:
                return True
            else:
                return False
        if y % 4 == 0 and y % 100 != 0:
            if d <= vYear[m-1]:
                return True
            else:
                return False
        elif y % 4 != 0 or y % 100 == 0 and y % 400 != 0:
            if d <= neVYear[m-1]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
print(date(29, 2, 2000))
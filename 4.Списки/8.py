day, month, year = list(map(int, input().split()))

vYear = tuple([31,29,31,30,31,30,31,31,30,31,30,31])
neVYear = tuple([31,28,31,30,31,30,31,31,30,31,30,31])

sum_date = 0
if year % 4 == 0:
    for x in range(month -1):
        sum_date += vYear[x]
elif year % 4 !=0:
    for z in range(month-1):
        sum_date += neVYear[z]
print(sum_date+day)
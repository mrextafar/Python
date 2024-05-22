count = 0
def SieveOfEratosthenes(_num):
    global count
    _list = list(range(2,_num+1))
    for i in _list:
        for j in _list:
            if j % i == 0 and i != j:
                count += 1
                _list.remove(j)
    return _list


num = 100
print(SieveOfEratosthenes(num)) # O(N^2)
print(count)
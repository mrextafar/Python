import random
count = 0
def BinarySearch(_arr,_value):#O(log(N))
    global count
    left = 0
    right = len(_arr) - 1

    while left <= right:
        count += 1
        center = (left + right) // 2
        if _value == _arr[center]:
            return center
            break
        if _value > _arr[center]:
            left = center + 1
        else:
            right = center - 1
    else:
        return "No Value"


arr = list(range(100000))
limitation = 9000
random.shuffle(arr)
newArr = arr[:limitation]
newArr.sort()
print("Array = ", newArr)
value = random.randint(0,100000)
print("Value = ", value)
print("ID = ", BinarySearch(newArr,value))
print("Count = ", count)
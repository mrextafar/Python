count = 0
def BubbleSort(_arr):
    global count
    i = 0
    for i in range(len(_arr)-1):
        for j in range(len(_arr) - 1 - i):
            if _arr[j] > _arr[j + 1]:
                count += 1
                _arr[j], _arr[j + 1] = _arr[j + 1], _arr[j]
    return _arr

arrSorted = [0,1,2,3,4,5,6,7,8,9]
print(BubbleSort(arrSorted), "Sorted") # O(N)
print(count)
count = 0
arrSortedBackwards = [9,8,7,6,5,4,3,2,1,0] # O(N^2)
print(BubbleSort(arrSortedBackwards),"SortedBackwards")
print(count)
count = 0
arrUnSorted = [0,9,1,8,2,7,3,6,4,5] # O(N)
print(BubbleSort(arrUnSorted), "Unsorted")
print(count)
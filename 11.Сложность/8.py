def SearchingForTheLargestIncreasingSubsequences(_arr):#O(N)
    count = 0
    maxCount = 0
    for i in range(1,len(_arr)):
        current = _arr[i-1]
        next = _arr[i]
        if current < next:
            count += 1
            if i == len(_arr)-1 and count > maxCount:
                maxLen = count
        else:
            if count > maxCount:
                maxCount = count
                maxLen = maxCount
                lastInMax = i
            count = 0
    maxLen += 1
    res = _arr[lastInMax - maxLen : lastInMax]
    return res

arr = [1,2,3,0,99,2,4,1,6,1,2,3,4,4,4,2,12,1,5]
print(SearchingForTheLargestIncreasingSubsequences(arr))
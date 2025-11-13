

# first merge the sorted array 
def mergeArray(leftArr, rightArr):
    # time complexity: o(n + m)
    # space complexity: o(n + m)
    result = []
    leftLength = len(leftArr)
    rightLength = len(rightArr)
    i = j = 0 # starting idx

    while i< leftLength and j < rightLength:
        if leftArr[i] <= rightArr[j]:
            result.append(leftArr[i])
            i += 1
        else:
            result.append(rightArr[j])
            j += 1
    if i < leftLength:
        while i < leftLength:
            result.append(leftArr[i])
            i+= 1
    if j< rightLength:
        while j < rightLength:
            result.append(rightArr[j])
            j+= 1
    return result
    
# leftArr = [2, 2, 4, 5]
# rightArr = [3, 3, 3, 7, 9]

# r = mergeArray(leftArr, rightArr)
# print(r)

# next do mergeSort
def mergeSort(arrNums):
    # time complexity : o(log N):
    # space complexity : o (n)
    if len(arrNums) == 1:
        return arrNums # single element array is sorted
    mid = len(arrNums) // 2
    leftArr = mergeSort(arrNums[:mid])
    rightArr = mergeSort(arrNums[mid:])
    return mergeArray(leftArr, rightArr)

arrNums = [7, 2, 5, 2, 9, 5, 1, 7, 4]

rr = mergeSort(arrNums)
# when you call the above time complexity:  o(n log N)
print(rr)
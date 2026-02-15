def merge(left, right):
    i = 0
    j = 0
    leftLength = len(left)
    rightLength = len(right)
    finalArr = []
    while i < leftLength and j < rightLength:
        if left[i] < right[j]:
            finalArr.append(left[i])
            i += 1
        else:
            finalArr.append(right[j])
            j += 1
    while i < leftLength:
        finalArr.append(left[i])
        i += 1
    while j < rightLength:
        finalArr.append(right[j])
        j += 1
    return finalArr


# left = [12, 18,]
# right = [3, 17, 22, 44]
# r = merge(left, right)
# print(r)

def mergeSortDevide(arr, start, end):
    if start == end:
        return [arr[start]]
    
    mid = (start+end)//2
    
    leftArr = mergeSortDevide(arr, start, mid)
    rightArr = mergeSortDevide(arr, mid+1, end)
    return merge(leftArr, rightArr)
    
    
data = [38, 27, 43, 10, 3, 9, 82, 10]
r = mergeSortDevide(data, 0, len(data)-1)
print(r)
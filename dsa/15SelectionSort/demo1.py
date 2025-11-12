def SelectionSort(arrNums, startIdx, minIdx):
    # time complexity = O(n^2), space complexity: o(1)
    pointer = startIdx+1 
    while startIdx < pointer and pointer < len(arrNums):
        while pointer < len(arrNums):
            if arrNums[pointer] < arrNums[minIdx]:
                minIdx = pointer
            pointer += 1

        arrNums[startIdx], arrNums[minIdx] = arrNums[minIdx], arrNums[startIdx]
        startIdx += 1
        minIdx = startIdx
        pointer = startIdx + 1
    pass

nums = [5, 7, 8, 4, 1, 6, 9, 2]
#       
startIdx = 0
minIdx = 0
SelectionSort(nums, startIdx, minIdx)
print(nums)

def selectionSortDescending(arrNums):
    # time complexity = O(n^2), space complexity: o(1)
    startIdx = maxIdx = 0
    pointer = 1
    while startIdx < pointer and pointer < len(arrNums):
        while pointer < len(arrNums):
            if arrNums[pointer] > arrNums[maxIdx]:
                maxIdx = pointer
            pointer += 1
        
        arrNums[startIdx], arrNums[maxIdx] = arrNums[maxIdx], arrNums[startIdx]
        startIdx += 1
        maxIdx = startIdx
        pointer = startIdx + 1

nums = [5, 7, 8, 4, 1, 6, 9, 2]
selectionSortDescending(nums)
print(nums)
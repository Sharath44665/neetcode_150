def insertionSort(arNums):
    # time complexity: o(n^2), space complexity: o(1)
    for pointIdx in range(1, len(arNums)):
        leftIdx = pointIdx - 1
        while leftIdx > -1:
            if arNums[pointIdx]< arNums[leftIdx]:
                arNums[pointIdx],arNums[leftIdx] =arNums[leftIdx],arNums[pointIdx]
            leftIdx -= 1
            pointIdx -= 1
    pass


arNums = [3, 5, 6, 4, 8, 9, 10, 7, 1]
insertionSort(arNums)
print(arNums)


def insertionSortTwo(arNums):
    for idx in range(1, len(arNums)):
        key = arNums[idx]
        j =  idx -1
        while j >= -1: # while j >= 0 
            if arNums[j] > key:
                arNums[j+1] =arNums[j]
            if arNums[j] < key:
                arNums[j+1] =key
                break
            if j == -1:
                arNums[j+1] =key
                break
            j -= 1
        

        
arNums = [3, 5, 6, 4, 8, 9, 10, 7, 1]
insertionSortTwo(arNums)
print(arNums)
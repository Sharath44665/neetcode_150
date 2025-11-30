def mergeTwoSortedArraysWithoutDuplicate(numOne, numTwo):
    numOneLength =  len(numOne)
    numTwoLength = len(numTwo)
    i = 0
    j = 0
    result = []
    
    while i< numOneLength and j < numTwoLength:
        if numOne[i] <= numTwo[j]:
            if len(result) == 0 or result[-1] != numOne[i]:
                result.append(numOne[i])
            i += 1
        else:
            if len(result) == 0 or result[-1] != numTwo[j]:
                result.append(numTwo[j])
            j += 1
    
    while i < numOneLength:
        if len(result) == 0 or result[-1] != numOne[i]:
                result.append(numOne[i])
        i += 1

    while j < numTwoLength:
        if len(result) == 0 or result[-1] != numTwo[j]:
            result.append(numTwo[j])
        j += 1

    return result
numOne = [-1, 1, 1, 2, 4, 6, 7]
numTwo = [1, 2, 3, 6, 7,  8, 9,9, 10]

r = mergeTwoSortedArraysWithoutDuplicate(numOne, numTwo)
print(r)
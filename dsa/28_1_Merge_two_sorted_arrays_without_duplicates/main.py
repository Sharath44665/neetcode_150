def mergeTwoSortedArraysWithoutDuplicate(numOne, numTwo):
    # time : o(N), space:o(N) where n is length of numOne or numTwo.
    
    result = []
    i  = 0
    j  = 0
    while i < len(numOne) and j < len(numTwo):
        if len(result)==0:
            if numOne[i] <= numTwo[j]:
                result.append(numOne[i])
                i += 1
            else:
                result.append(numTwo[j])
                j += 1
            
        resultLength =  len(result) 

        if result[resultLength-1] == numOne[i] and result[resultLength-1] == numTwo[j]:
            i += 1
            j += 1
        elif numOne[i] <= result[resultLength-1]  and result[resultLength-1] != numTwo[j] :
            i += 1
        elif result[resultLength-1] != numOne[i] and numTwo[j] <= result[resultLength-1]:
            j += 1
        elif numOne[i] > result[resultLength-1] and numOne[i]==numTwo[j]:
            result.append(numOne[i])
            i += 1
            j += 1
        elif numOne[i] > result[resultLength-1] and numOne[i] < numTwo[j]:
            result.append(numOne[i])
            i += 1
        elif numTwo[j] > result[resultLength-1] and numTwo[j] < numOne[i]:
            result.append(numTwo[j])
            j += 1

    # add the remaining
    while j < len(numTwo):
        resultLength =  len(result)
        if numTwo[j] > result[resultLength - 1]:
            result.append(numTwo[j])
        j += 1

    while i < len(numOne):
        resultLength =  len(result)
        if numOne[i] > result[resultLength - 1]:
            result.append(numTwo[i])
        j += 1


    return result

numOne = [-1, 1, 1, 2, 4, 6, 7]
numTwo = [1, 2, 3, 6, 7,  8, 9,9, 10]

r = mergeTwoSortedArraysWithoutDuplicate(numOne, numTwo)
print(r)
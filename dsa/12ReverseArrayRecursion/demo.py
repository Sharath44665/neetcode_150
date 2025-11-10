def doReverseArray(arr, myArrayLength, reverseArr):
    # time complexity o(N), space complexity o(N) where n is the length of array
    if myArrayLength < 1:
        return
    reverseArr[myArrayLength-1]= arr[len(reverseArr)-myArrayLength]
    doReverseArray(arr, myArrayLength-1, reverseArr)
    

myArr = [1, 2, 3, 4, 5]
myArrayLength = len(myArr)
reverseArr=[0 for _ in myArr]
doReverseArray(myArr, myArrayLength, reverseArr)
print(reverseArr)

def makeReverseArray(arr, reverseArr, firstIdx, lastIdx):
    # time complexity o(N), space complexity o(N) where n is the length of array
    if firstIdx > lastIdx:
        return
    # reverseArr[firstIdx]= arr[lastIdx]
    # reverseArr[lastIdx] = arr[firstIdx]
    reverseArr[firstIdx],reverseArr[lastIdx] = arr[lastIdx], arr[firstIdx]
    makeReverseArray(arr, reverseArr, firstIdx+1, lastIdx-1)
    pass

myArr = [1, 2, 3, 4, 5]
firstIdx = 0
lastIdx = len(myArr)-1
reverseArr = [0 for _ in myArr]
makeReverseArray(myArr, reverseArr, firstIdx, lastIdx)
print(reverseArr)


def makeReverseArrayTwo(arr, firstIdx, lastIdx):
    if firstIdx > lastIdx:
        return
    # reverseArr[firstIdx]= arr[lastIdx]
    # reverseArr[lastIdx] = arr[firstIdx]
    arr[firstIdx],arr[lastIdx] = arr[lastIdx], arr[firstIdx]
    makeReverseArray(arr, reverseArr, firstIdx+1, lastIdx-1)

myArr = [1, 2, 3, 4, 5]
firstIdx = 0
lastIdx = len(myArr)-1

makeReverseArrayTwo(myArr, firstIdx, lastIdx)
print(myArr)


# using while loop
def loopReverseArray(arr):
    startIdx = 0 
    lastIdx = len(arr)-1

    while startIdx < lastIdx:
        arr[startIdx],arr[lastIdx] = arr[lastIdx], arr[startIdx]
        startIdx += 1
        lastIdx -= 1

arr = [1,2,3,4,5]
loopReverseArray(arr)
print(arr)
def findSecondLargest(nums):
    # time complexity: o(N), space: o(1)
    firstLargest = findLargest(nums)
    secondMaxValue = maxElement  = nums[0]
    startIdx = 1
    lastIdx = len(nums)-1
    while startIdx < lastIdx:  
        if nums[startIdx] > nums[lastIdx] and nums[startIdx]< firstLargest:
            maxElement = nums[startIdx]
        else:
            maxElement = nums[lastIdx]
         
        if maxElement > secondMaxValue and maxElement < firstLargest:
            secondMaxValue = maxElement
        
        startIdx += 1
        lastIdx -= 1

    return secondMaxValue
    

def findLargest(nums):
    # time complexity: o(N), space: o(1)
    maxValue = nums[0]
    startIdx = 0 
    lastIdx = len(nums)-1

    while startIdx < lastIdx:
        if nums[startIdx] > nums[lastIdx]:
            maxElement = nums[startIdx]
        else:
            maxElement = nums[lastIdx]
        
        if maxElement > maxValue:
            maxValue = maxElement
        startIdx += 1
        lastIdx -= 1
    return maxValue

nums = [ 55, 32, 97, 45, 32, 88, 21]
secondMax = findSecondLargest(nums)
print(secondMax)


def findSecondLargestList(nums):
    firstMax = findLargest(nums)
    secondMax = nums[0]
    for val in nums:
        if val > secondMax and val < firstMax:
            secondMax = val
    return secondMax

max2 = findSecondLargestList(nums)
print(max2)

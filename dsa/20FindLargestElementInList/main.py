def findLargestElement(nums):
    # time complexity = o(N), space: o(1)
    maxValue = nums[0]
    for val in nums:
        if val > maxValue:
            maxValue = val

    return maxValue 

nums = [55, -97, 99, 3, 67]
maxValue = findLargestElement(nums)
print(maxValue)


def findLargest(nums):
    # time complexity = o(N), space: o(1)
    # maxValue = nums[0]
    maxValue = float("-inf")
    startIdx = 1
    endIdx = len(nums)-1

    while startIdx <= endIdx:
        if nums[startIdx] < nums[endIdx]:
            maxElement = nums[endIdx]
        else:
            maxElement = nums[startIdx]
        
        if maxElement > maxValue:
            maxValue = maxElement
        startIdx += 1
        endIdx -= 1
    return maxValue

val = findLargest(nums)
print(val)

def findLargestFromList(nums):
    val = max(nums)
    return val

val = findLargestFromList(nums)
print(val)

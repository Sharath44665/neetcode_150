def isArraySorted(nums):
    # assuming sorted ascending order
    # time complexity: o(n), space complexity: o(1)
    startIdx = 0
    lastIdx = len(nums) - 1

    while startIdx < lastIdx:
        if nums[startIdx] > nums[startIdx + 1] or nums[lastIdx] < nums[lastIdx - 1]:
            return False
        startIdx += 1
        lastIdx -= 1
    return True
    

nums = [-5, -3, -1, 0, 22, 4, 6]
print(isArraySorted(nums))
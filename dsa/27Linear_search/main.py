def linearSearch(nums, element):
    # time : o(N), space: o(1)
    for idx in range(len(nums)):
        if nums[idx] == element:
            return idx
    return -1


nums = [0, 5, 7, 12, 15, 22, 30, 44, 58, 63, 77, 89]
found = linearSearch(nums=nums, element=22)
print(found)

nums = [-2, 3, -1, 5, -2, 7, -3, 3, -1, 6, 5, -4]
found = linearSearch(nums=nums, element=-2) # whatever the first occurence idx should return
print(found)

def improvedLinearSearch(nums, element):
    # time : o(N), space: o(1) 
    startIdx = 0
    endIdx = len(nums)-1

    while startIdx < endIdx:
        if nums[startIdx] == element:
            return startIdx
        elif nums[endIdx] == element:
            return endIdx
        startIdx += 1
        endIdx -= 1
    return -1

# above code does not returns idx whatever the first occurence idx
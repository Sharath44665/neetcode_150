def moveZeros(nums):
    # time : o(N), space: o(N)
    tempArr = []
    for val in nums:
        if val != 0:
            tempArr.append(val)

    for idx in range(len(nums)):
        if idx >= len(tempArr):
            nums[idx] = 0
        else:
            nums[idx]= tempArr[idx]

    
    pass

nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
moveZeros(nums)
print(nums)
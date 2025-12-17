def trasnposeSquareMatrix(nums):
    print("before")
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            print(nums[i][j], end=" ")
        print()

    print("--- after ---")

    i = j = 0
    while i < len(nums):
        j = i
        while j < len(nums[i]): 
            nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
            j += 1
        i += 1
    
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            print(nums[i][j], end=" ")
        print()

def transposeAnyMatrix(nums):
    res = []

    i = j = 0
    length = len(nums)
    while i < len(nums[0]):
        j = 0
        res.append([])
        while j < length:
            res[i].append(nums[j][i])
            j += 1
        i += 1
    
    print("after transpose:")
    for val in res:
        for idx in range(len(val)):
            print(val[idx], end=" ")
        print()

nums = [[5, 8, 9], [1, 7, 6], [3, 1, 2]]
# nums = [[5, 8, 1, 3], [7, 6, 3, 4], [2, 1, 9, 8], [5, 2, 1, 3]]
# trasnposeSquareMatrix(nunums[j][i]ms)
nums = [[5, 9, 1], [2, 3, 7]]
transposeAnyMatrix(nums)
# [5 8 9]         [5 1 3]
# [1 7 6]    =>   [8 7 1] 
# [3 1 2]         [9 6 2]

# [5, 9, 1]   => 5 2
# [2, 3, 7]      9 3
#                1 7
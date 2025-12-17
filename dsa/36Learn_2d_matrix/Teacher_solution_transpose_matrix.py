def transposeMatrix(nums):
    rows = len(nums)
    cols = len(nums[0])
    result = [[0 for _ in range(rows)] for _ in range(cols) ] # if original matrix is 3X2, result matrix will be 2X3

    print(result)
    for i in range(rows):
        for j in range(cols):
            result[j][i] = nums[i][j]
    
    
    for val in result:
        for v in val:
            print(v, end= " ")
        print()

nums = [[5, 9, 1], [2, 3, 7]]
transposeMatrix(nums)
    
def printLowerTriangle(nums):
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if i >= j:
                print(nums[i][j], end=" ")
            else:
                print("*", end= " ")
        print()

# nums = [[5, 10, 11], [7, 6, 3], [2, 1, 9]]
nums = [[5, 10, 1, 3], [7, 6, 3, 4], [2, 1, 9, 8], [5, 10, 1, 3]]
printLowerTriangle(nums)
def printUpperTriangle(nums):
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if  j>=i:
                print(nums[i][j], end= " ")
            else:
                print("*", end= " ")
        print()
    pass


nums = [[5, 10, 11], [7, 6, 3], [2, 1, 9]]
# nums = [[5, 10, 1, 3], [7, 6, 3, 4], [2, 1, 9, 8], [5, 10, 1, 3]]
printUpperTriangle(nums)
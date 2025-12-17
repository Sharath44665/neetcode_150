def printDiagonalTriangle(nums):
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if i == j:
                print(nums[i][j], end=" ")
            else:
                print("*", end=" ")
        print()

def printAnotherDiagonalTriangle(nums):
    counter = len(nums)-1
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if j == counter:
                print(nums[i][j], end=" ")
            else:
                print("*", end= " ")
        counter -= 1
        print()

# nums = [[5, 10, 11], [7, 6, 3], [2, 1, 9]]
nums = [[5, 10, 1, 3], [7, 6, 3, 4], [2, 1, 9, 8], [5, 10, 1, 3]]
printDiagonalTriangle(nums)
print("----")
printAnotherDiagonalTriangle(nums)
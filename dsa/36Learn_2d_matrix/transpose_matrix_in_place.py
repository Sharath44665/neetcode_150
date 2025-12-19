def transposeMatrixInplace(matrix):
    # only works for square matrix
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# matrix = [
#     [1, 3],
#     [2, 4],
#     [5, 7], 
# ]
transposeMatrixInplace(matrix)
print(matrix)
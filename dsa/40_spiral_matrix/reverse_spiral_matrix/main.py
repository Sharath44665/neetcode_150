# inspired by spiral matrix

def reverseSpiralMatrix(matrix):
    top, left = 0, 0
    bottom, right = len(matrix)-1, len(matrix[0])-1
    result = []
    while top <= bottom and left <= right:
        # right to left
        for i in range(right, left-1, -1):
            result.append(matrix[top][i])
        top += 1
        # top to bottom
        for i in range(top,bottom+1):
            result.append(matrix[i][left])
        left += 1

        # bottom left to bottom right
        if left <= right:
            for i in range(left, right+1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # bottom right to top right
        if top <= bottom: # something wrong
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][right])
            right -= 1
        
    print(result)
    


matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13, 14, 15, 16]
    ]

reverseSpiralMatrix(matrix)


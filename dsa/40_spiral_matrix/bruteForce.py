class Solution(object):
    def spiralOrder(self, matrix):
        result = [ ]
        top, left = 0, 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # fill the top row
            for i in range(left, right+1):
                result.append( matrix[left][i] )
            top += 1

            # fill the last column
            for i in range(top, bottom +1):
                result.append(matrix[i][right])
            right -= 1

            # fill the last row
            if top <= bottom:
                for i in range(right, left -1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            # fill the first colum
            if left <= right:
                for i in range(bottom, top -1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result


matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13, 14, 15, 16]
    ]


s = Solution()
r = s.spiralOrder(matrix)
print(r)
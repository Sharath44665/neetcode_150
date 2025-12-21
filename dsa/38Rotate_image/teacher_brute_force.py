# not in place

class Solution(object):
    def rotate(self, matrix):
        # time complexity: o(n^2), space: o(n^2)
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """ 
        result = [[0 for _ in matrix[0]]for _ in matrix]
        counter = len(matrix) -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[j][counter] = matrix[i][j]
            counter -= 1

        print(result)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# answer = [
#     [13, 9, 5, 1],
#     [14, 10, 6,  2],
#     [15, 11, 7, 3],
#     [16, 12, 8, 4]
# ]

s = Solution()
s.rotate(matrix)
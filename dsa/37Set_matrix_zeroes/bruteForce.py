class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # time: o(N), space:o(N)

        findZeros = []
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    findZeros.append((i,j))

        for val in findZeros: # fill zeros 
            m, n = val
            for i in range(rows):
                for j in range(cols):
                    if m == i:
                        matrix[i][j] = 0
                    if n == j:
                        matrix[i][j] = 0

        
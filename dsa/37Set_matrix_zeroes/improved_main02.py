class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
#         """
        # time: o(N), space:o(1)
        firstRow = False
        firstCol = False
        r = len(matrix)
        c = len(matrix[0])
        # check first row zero?
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                firstRow = True
        

        # check first col zero?
        for i in  range(len(matrix)):
            if matrix[i][0] == 0:
                firstCol = True

        # check inside element zero, if yes, make first row/col position zero
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0 #first row
                    matrix[i][0] = 0

        # now fill zeros for cols and rows of above matrix
        for i in range(1, r):
            for j in range(1,c):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if firstRow:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        
        if firstCol:
            for i in range(len(matrix)):
                matrix[i][0] = 0

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # time: o((n+m) * (n*m)), space: o(1)
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m): #o(n*m)
            for j in range(n):
                if matrix[i][j] == 0: # time: o(n+m)
                    for u in range(0,m):
                        if matrix[u][j] == 0: # skip for repetitive zero
                            continue
                        matrix[u][j] = "a" # teacher said to put infinity
                    
                    for v in range(0,n):
                        if matrix[i][v] == 0:
                            continue
                        matrix[i][v] = "a"
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "a":
                    matrix[i][j] = 0





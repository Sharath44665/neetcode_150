class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        colTrack = [0 for _ in range(len(matrix[0]))]
        rowTrack = [0 for _ in range(len(matrix))]
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    colTrack[j] = -1 # make col track idx -1
                    rowTrack[i] = -1 # make row track idx -1

        for i in range(n):
            for j in range(m):
                if colTrack[j] == -1 or rowTrack[i] == -1: # if col track or row track has -1 make that cell zero
                    matrix[i][j] = 0




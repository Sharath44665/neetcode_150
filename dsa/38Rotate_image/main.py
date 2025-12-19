# worked in first try 😂
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """ 
        # time:(o(n*m)), space: o(1)
        rows = len(matrix)
        cols = len(matrix[0])

        # first trasponse matrix
        for i in range(rows):
            for j in range(i+1, cols):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
       
        
        # then reverse all the elements in matrix:
        for nums in matrix:
            i = 0
            j = len(nums)-1

            while i < j:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1




        
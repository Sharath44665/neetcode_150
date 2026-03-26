class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
   
        result = []
        spiralCheck = [[0 for _ in matrix[0]] for _ in matrix]

        topEnd = len(matrix[0])
        rightEnd = len(matrix)

        for i in range(len(matrix)):
            topStart = i
            rightStart = i+1
            bottomStart = topEnd - 2
            bottomEnd = topStart
            leftStart = rightEnd-1
            leftEnd = i+1

            if len(matrix[0]) == 1:
                while topStart < len(matrix):
                    result.append(matrix[topStart][i])
                    topStart += 1
                break
            
            

            while topStart < topEnd:
                if spiralCheck[i][topStart] == -1:
                    break
                result.append(matrix[i][topStart])
                spiralCheck[i][topStart] = -1
                topStart += 1
            
            while topEnd > 1 and rightStart < rightEnd:# and topStart != rightStart:
                if spiralCheck[rightStart][topEnd-1] == -1:
                    break
                result.append(matrix[rightStart][topEnd-1])
                spiralCheck[rightStart][topEnd-1] = -1
                rightStart += 1

            while rightEnd > 1 and bottomStart > bottomEnd:
                if spiralCheck[rightEnd-1][bottomStart] == -1:
                    break
                result.append(matrix[rightEnd-1][bottomStart])
                spiralCheck[rightEnd-1][bottomStart] = -1
                bottomStart -= 1

            while  topEnd > 1 and leftStart >= leftEnd:
                if spiralCheck[leftStart][i] == -1:
                    break
                result.append(matrix[leftStart][i])
                spiralCheck[leftStart][i] = -1
                leftStart -= 1
            
        
            topEnd -= 1
            rightEnd -= 1
        return result

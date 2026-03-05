class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minNum= 0
        maxNum = nums[0]
        checker = {}

        for val in nums:
            if val < minNum:
                minNum = val
            
            if val > maxNum:
                maxNum = val
            checker[val] = 1

        while  minNum <= maxNum:
            if minNum not in checker:
                return minNum
            minNum += 1
        return minNum
        

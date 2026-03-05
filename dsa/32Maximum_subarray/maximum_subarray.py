class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time : o(N), space: o(1)
        maxSum = nums[0]
        sum = 0

        for val in nums:
            sum += val
            if val > sum:
                sum = val
            
            if sum > maxSum:
                maxSum = sum

        return maxSum
        

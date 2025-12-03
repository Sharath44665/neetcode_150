class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # time: o(N), space: o(1)
        maxSum = nums[0]
        total = idx = 0
        while idx < len(nums):
            total += nums[idx]
            if total > maxSum:
                maxSum = total
            if total < 0:
                total = 0
            
            idx += 1
        return maxSum
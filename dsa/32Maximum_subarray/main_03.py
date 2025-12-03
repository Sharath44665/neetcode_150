class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        maxSum = nums[0]

        for idx in range(1,len(nums)):
            currentSum += nums[idx]
            # if nums[idx] > currentSum: # positive num > negative num
            #     currentSum = nums[idx]
            currentSum = max(nums[idx], currentSum) # alternative to above two lines
            
            # if currentSum > maxSum:
            #     maxSum = currentSum
            maxSum = max(currentSum, maxSum)  # alternative to above two lines
        return maxSum
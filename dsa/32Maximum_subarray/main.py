class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # time: o(N), space: o(1)
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2 and nums[0] < 0 and nums[1]< 0:
            if nums[0] < nums[1]:
                return nums[1]
            return nums[0]
        
        idx = 1 
        sum = nums[idx-1]
        currentSum = nums[idx-1]
        while idx < len(nums):
            prevSum = currentSum
            currentSum += nums[idx]

            if nums[idx] > currentSum:
                currentSum = nums[idx] 
            
            if prevSum > currentSum and prevSum > sum:
                sum = prevSum

            idx += 1

        if currentSum > sum:
            return currentSum

        return sum

        

# nums = [31,-41,59,26,-53,58,97,-93,-23,84]
# nums = [-2,-3,-1]
# s = Solution()
# r = s.maxSubArray(nums)
# print(r)
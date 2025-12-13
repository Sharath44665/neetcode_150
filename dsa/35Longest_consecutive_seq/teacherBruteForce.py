class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxCount = 0

        for i in range(0,n):
            num = nums[i]
            count = 1
            while num+1 in nums:
                count +=1
                num += 1
            maxCount = max(maxCount, count)
        return maxCount

# nums = [0,3,7,2,5,8,4,6,0,1] # expected 9
nums = [-4,-1,4,-5,1,-6,9,-6,0,2,2,7,0,9,-3,8,9,-2,-6,5,0,3,4,-2] # expected 12


s = Solution()
r = s.longestConsecutive(nums)
print(r)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [i, hashmap[diff]]
            hashmap[nums[i]] = i
        # Return an empty list if no solution is found
        return []

s = Solution()
nums = [2, 7, 11, 15]
target = 9
print(s.twoSum(nums, target))
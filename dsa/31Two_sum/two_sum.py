class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        existCheck = {}
        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in existCheck:
                return [idx, existCheck[diff]]
            else:
                existCheck[nums[idx]] = idx
        

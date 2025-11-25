class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # time : o(N), space: o(N)
        if len(nums) == 1:
            return nums
        length = len(nums)
        k = k % length
        nums[:] = nums[length-k:]+nums[0:length-k]
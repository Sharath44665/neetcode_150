class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # time: o(N), space: o(1)
        k = k % len(nums)

        # reverse the whole array
        nums.reverse()

        # reverse first k elements
        nums[:k] = reversed(nums[:k])

        # reverse remaining elements
        nums[k:] = reversed(nums[k:])
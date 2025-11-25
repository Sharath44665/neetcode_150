class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # time: o(N), space: o(1)
        startIdx = 0
        length = len(nums)
        endIdx =length - 1
        self.reverseArray(nums, startIdx, endIdx)
        
        k = k % length
        
        #   [1, 2, 3, 4, 5, 6, 7]
        # 3 [7, 6, 5, 4, 3, 2, 1]
        
        self.reverseArray(nums, startIdx, k-1)

        self.reverseArray(nums, k, endIdx)

    def reverseArray(self, nums, startIdx, endIdx):
       
        while startIdx < endIdx:
            nums[startIdx],nums[endIdx] = nums[endIdx], nums[startIdx]
            startIdx += 1
            endIdx -= 1
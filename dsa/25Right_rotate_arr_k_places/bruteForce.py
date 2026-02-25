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
        tempArray = []
        startIdx = length-k

        while startIdx < length:
            tempArray.append(nums[startIdx])
            startIdx += 1 

        endIdx = length-1
        startIdx = length-1-k # [1,2,3,4,5,6,7]
        while startIdx >= 0:
            nums[endIdx] = nums[startIdx]
            startIdx -= 1
            endIdx -= 1
        
        startIdx =0 
        while startIdx < k:
            nums[startIdx]=tempArray[startIdx]
            startIdx += 1
        pass
    
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        firstPart = []
        secondPart = []

        for idx in range(len(nums)-k, len(nums)):
            firstPart.append(nums[idx])

        for idx in range(0, len(nums)-k):
            secondPart.append(nums[idx])
        
        sidx = 0
        for idx in range(len(nums)):
            if idx < len(firstPart):
                nums[idx] =firstPart[idx]
            else: 
                nums[idx] = secondPart[sidx]
                sidx += 1

        

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Memory Limit Exceeded
        #  here logic is store everything, store unique data, keep track of minVal and maxVal, loop from min to max and find the longest sequence.
        storeUniqueData = {}
        minVal  = nums[0]
        maxVal = nums[0]
        longSeq = 0
        for idx in range(len(nums)):
            minVal = min(minVal, nums[idx])
            maxVal = max(maxVal, nums[idx])
            storeUniqueData[nums[idx]] = idx
        
        counter = 0

        # print(storeUniqueData)

        for val in range(minVal,maxVal+1):
            if val not in storeUniqueData:
                counter = 0
                continue
            if val in storeUniqueData:
                counter += 1
                longSeq = max(longSeq, counter)
        
        return longSeq

nums = [0,3,7,2,5,8,4,6,0,1, 99] # expected 9
# nums = [-4,-1,4,-5,1,-6,9,-6,0,2,2,7,0,9,-3,8,9,-2,-6,5,0,3,4,-2] # expected 12


s = Solution()
r = s.longestConsecutive(nums)
print(r)
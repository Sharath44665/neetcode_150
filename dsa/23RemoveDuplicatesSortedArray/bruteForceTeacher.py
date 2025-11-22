class Solution(object):
    # does not work for negative numbers
    def removeDuplicates(self, nums):
        storeDict = {}
        for val in nums:
            if val not in storeDict:
                storeDict[val] = 0
        idx  = 0
        for key in storeDict:
            nums[idx] = key
            idx += 1
        

        pass



nums = [1,1,2, 3, 4, 4, 7, 9, 9, 9, 9, 10]
s = Solution()
s.removeDuplicates(nums)
print(nums)
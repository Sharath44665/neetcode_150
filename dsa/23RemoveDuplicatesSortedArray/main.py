class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        idx  = 0
        while idx < len(nums) -1:
            nextIdx = idx + 1
            while nums[nextIdx] ==  nums[idx]:
                nums[nextIdx] = ""
                nextIdx += 1
                if nextIdx >= len(nums):
                    break
            idx = nextIdx
        
        idx = 0
        while idx < len(nums):
            if nums[idx] != "":
                k += 1 
            idx += 1 
        
        i = j =0 
        while i< len(nums) and j < len(nums): # [2, _, _ , 3, -, -, 4]
            if nums[i] != "":
                i += 1
                j += 1
            elif nums[j] == "":
                j += 1
            elif nums[j] != "" and i != j:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j += 1
        return k
            
nums = [1,1]
s = Solution()
s.removeDuplicates(nums)
print(nums)
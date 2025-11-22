class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = i = 0
        j  = i + 1 

        length = len(nums)
        while i < length and j< length: # [1, 1,1 ,3, 3]
            if nums[i] != nums[j]:
                nums[i+1],nums[j] = nums[j], nums[i+1]
                i += 1
                j += 1
            else:
                j += 1
        k = i
        return k+1

# nums = [1,1,2, 3, 4, 4, 7, 9, 9, 9, 9, 10]
nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
s.removeDuplicates(nums)
print(nums)

class SolutionImproved(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j  = i + 1 
        length = len(nums)
        while j< length: # [1, 1,1 ,3, 3]
            if nums[i] != nums[j]:
                nums[i+1],nums[j] = nums[j], nums[i+1]
                i += 1
            j += 1
        k = i
        return k+1
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # in place solution
        
        i = 0

        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] >= 0 and nums[j] < 0:
                    temp = nums[i+1]
                    nums[i+1] = nums[j]

                    while j > i+2:
                        nums[j] = nums[j-1]
                        j -= 1
                    nums[j] = temp
                    # nums[i+1],nums[j] = nums[j],nums[i+1]
                    break
                if nums[i] < 0 and nums[j] >= 0:
                    nums[i],nums[j] = nums[j],nums[i]
                elif nums[i] >= 0 and nums[j] >= 0:
                    j += 1
            i += 2

        return nums
    




nums = [3,1,2,5,-2,-5,-4, -1]
s= Solution()
s.rearrangeArray(nums)
print(nums)

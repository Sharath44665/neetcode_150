class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 1
        i = 0
        j = i + 1

        # nums = [0,0,1,1,1,2,2,3,3,4]
        while i < j and j < len(nums):
            if nums[i] == nums[j]:
                nums[j] = "_"
                j += 1
            elif nums[i] != nums[j]:
                counter += 1
                i += 1
                nums[i],nums[j] = nums[j],nums[i]
                j += 1
            else:
                i += 1
                j += 1
        # print(nums)
        # print(counter)
        return counter

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        # find unique
#         counter = 1
#         for idx in range(len(nums)-1):
#             if nums[idx] != nums[idx+1]:
#                 counter += 1
            # put underscore
#         idx = 0
#         while idx < len(nums)-1:
#             if nums[idx] == nums[idx+1]:
#                 nums[idx] = "_"
            
#             idx += 1

            # rearrange in right position
#         i = 0
#         j = i + 1
#         while i < j and j < len(nums):
#             if nums[i] == "_" and nums[j] != "_":
#                 nums[i],nums[j] =  nums[j],nums[i]
#                 i += 1
#                 j += 1
#             elif nums[i] =="_" and nums[j] == "_":
#                 j += 1
#             else:
#                 i += 1
#                 j += 1

#         return counter
        
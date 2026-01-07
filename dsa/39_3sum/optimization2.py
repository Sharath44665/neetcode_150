class Solution(object):
    def threeSum(self, nums):

        """ 
        :type nums: List[int] 
        :rtype: List[List[int]] 
        """ 
        # time:o(n^2), space: o(number of triplets)
        nums = sorted(nums)
        i = 0
        length = len(nums)
        result = []
        while i < length:
            if i != 0 and nums[i-1] == nums[i]:
                i += 1
                continue
            j = i+1
            k = length -1
            while j < k:
                total = nums[i]+ nums[j]+ nums[k]
                if total ==0:
                    result.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1 
                    # skip the duplicates
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                    while j < k and nums[k+1] == nums[k]:
                        k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -=1
            i +=1
        return result
# class Solution(object):
#     def threeSum(self, nums):

#         """ 
#         :type nums: List[int] 
#         :rtype: List[List[int]] 
#         """ 
#         # time:o(n^2), space: o(1)
#         nums = sorted(nums)
#         i = 0
#         length = len(nums)
#         result = set()
#         while i < length:
#             if i != 0 or nums[i-1] == nums[i]:
#                 i += 1
#                 continue
#             j = i+1
#             k = length -1
#             while j < k:
#                 if nums[i]+ nums[j]+ nums[k] ==0:
#                     result.add((nums[i], nums[j], nums[k]))
#                     j += 1
#                     k -= 1
#                 elif nums[i]+ nums[j]+ nums[k] < 0:
#                     j += 1
#                 else:
#                     k -=1
#             i +=1
#         return [ list(v) for v in result]


# n = [-2,0,1,1,2]
n = [-1,0,1,2,-1,-4]
s = Solution()
r = s.threeSum(n)
print(r)

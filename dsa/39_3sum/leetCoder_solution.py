class Solution(object):
 def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lis = []
        nums = sorted(nums)

        for i in range (0, len(nums)):
            if i > 0  and nums[i]==nums[i-1]:
                continue

            pointer1 = i+1
            pointer2 = len(nums)-1
            while pointer1<pointer2:
                if nums[pointer1]+nums[pointer2]==-nums[i]:
                   lis.append([nums[pointer1], nums[pointer2], nums[i]])

                   while pointer1<pointer2 and nums[pointer1]==nums[pointer1+1]:
                    pointer1+=1
                   while pointer1<pointer2 and nums[pointer2]==nums[pointer2-1]:
                    pointer2-=1
                   pointer1 +=1
                   pointer2 -=1
                elif nums[pointer1]+nums[pointer2]<=-nums[i]:
                   pointer1 +=1
                else:
                   pointer2 -=1
    
        return lis
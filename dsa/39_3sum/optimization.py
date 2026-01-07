class Solution(object):
    def threeSum(self, nums):

        """ 
        :type nums: List[int] 
        :rtype: List[List[int]] 
        """ 
        # time: o(n^2), space: o(n)
        i = 0 
        length = len(nums) 
        seen =set() 
        triplets = set() 
        while i < length: 
            j = i + 1 
            while j < length: 
                val = -(nums[i]+nums[j]) 
                if val in seen: 
                    v = sorted([nums[i], nums[j], val]) # time complexity for sorting we are ignoring this because of just 3 values, we can do it in o(1) operation
                    v = tuple(v) 
                    triplets.add(v) 

                seen.add(nums[j]) 
                j += 1 
            seen = set() 
            i+= 1


        return list( list(v) for v in triplets)

nums = [-1,0,1,2,-1,-4]
s= Solution()
r = s.threeSum(nums)
print(r)


# rough work
def sortThreeNums(nums):
    if nums[0]>nums[1]:
        nums[0],nums[1] = nums[1],nums[0]
    if nums[0] > nums[2]:
        nums[0],nums[2] =nums[2],nums[1]
    if nums[1] > nums[2]:
        nums[1], nums[2] = nums[2],nums[1]

n = [3, 1, 2]
n = [2, 1, 3]
sortThreeNums(n)
print(n)
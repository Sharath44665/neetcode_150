class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #time: o(n^3), space: o(n)
        #[-1,0,1,2,-1,-4]
        #[-1,0, 1] = 0
        #[2, -1, 1] = 0
        answer = []
        sum =  -1
        length =  len(nums)

    
        i = 0
        while i < length:
            j = i+ 1
            while j < length:
                k = j + 1
                while k < length:
                    sum = nums[i]+nums[j]+nums[k]
                    if sum == 0:
                        answer.append([nums[i],nums[j],nums[k]])
                    k += 1
                j += 1
            i += 1

    
        # remove duplicates
        temp = answer
        answer = []
        seen = set()
        for val in temp:
            v = set(val)
            v = tuple(v)
            if v not in seen:
                seen.add(v)
                answer.append(val)
        return answer

nums = [-1,0,1,2,-1,-4]
s = Solution()
s.threeSum()
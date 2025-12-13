class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time: o(N), space: o(N)
        numSet = set(nums)
       
        if len(numSet) == 1:
            return 1
        if len(numSet) == 0:
            return 0
        counter = 0
        seq = 1
        for val in numSet:
            if val-1 not in numSet:
                counter = 1
                minVal = val
                while minVal+1 in numSet:
                    counter += 1
                    seq = max(counter, seq)
                    minVal += 1

        return seq
       
# nums = [0,3,7,2,5,8,4,6,0,1] # expected 9
nums = [-4,-1,4,-5,1,-6,9,-6,0,2,2,7,0,9,-3,8,9,-2,-6,5,0,3,4,-2] # expected 12


s = Solution()
r = s.longestConsecutive(nums)
print(r)
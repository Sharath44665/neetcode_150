class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time: o(n^2), space: o(n)
        # my logic is res = [{1, 2}, {-1, 1, 2}] and find the return the max length
        idx = 0
        length = len(nums)
        maxSeq  =  0
        seq = {} # not required
        res = []
        while idx < length:
            tempIdx =  idx
            # if nums[idx] in seq:
            #     idx += 1
            #     continue
            j = 0
            seqTwo = {}
            while j < length:
                if nums[idx] == nums[j] + 1 and nums[j] not in seqTwo: 
                    seq[nums[idx]] = idx
                    seq[nums[j]]= j
                    seqTwo[nums[idx]] = idx
                    seqTwo[nums[j]] = j
                    idx = j
                    j = 0
                elif nums[idx] == nums[j] - 1 and nums[j] not in seqTwo: 
                    seq[nums[idx]] = idx
                    seq[nums[j]]= j
                    seqTwo[nums[idx]] = idx
                    seqTwo[nums[j]] = j
                    idx =  j
                    j = 0
                else:
                    j += 1
            idx = tempIdx
            res.append(seqTwo)
            idx += 1
        # print(seq)
        # print(res)

        for val in res:
            maxSeq = max(maxSeq, len(val))
        return maxSeq

        
nums = [100,4,200,1,3,2, 101]
nums = [1,0,1,2]
nums = [-4,-1,4,-5,1,-6,9,-6,0,2,2,7,0,9,-3,8,9,-2,-6,5,0,3,4,-2] # expected 12
s = Solution()
r = s.longestConsecutive(nums)
print(r)
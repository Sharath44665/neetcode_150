class Solution2:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # time: o(N), space: o(N)
        result = [0 for _ in nums]
        
        posIdx = 0
        negIdx = 1
        for val in nums:
            if val > 0: 
                result[posIdx] = val
                posIdx += 2
            else:
                result[negIdx] = val
                negIdx += 2

        return result

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # time: o(N), space: o(N)
        # [3,1,-2,-5,2,-4]
        posNums = []
        negNums = []
        for val in nums:
            if val > 0:
                posNums.append(val)
            else:
                negNums.append(val)

        i = 0
        j = 0
        idx  = 0 
        while idx < len(nums):
            if idx%2 ==0:
                nums[idx] = posNums[i]
                i += 1
            else:
                nums[idx] = negNums[j]
                j += 1

            idx += 1
        
        return nums


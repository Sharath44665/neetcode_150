class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time: o(N), space: o(N)
        result = {}
        for idx in range(len(nums)):
            result[nums[idx]] = idx
        
        for idx in range(len(nums)):
            find = target - nums[idx]
            if find in result and idx != result[find]:
                return [idx, result[find]]

        return []

class Solution:
    def twoSumOne(self, nums: List[int], target: int) -> List[int]:
        # time: o(n^2), space: o(1)
        startIdx = 0
        length = len(nums)
        while startIdx < length:
            nextIdx = startIdx + 1
            if nums[startIdx] > target:
                nextIdx = startIdx + 1
            while nextIdx < length:
                if nums[startIdx] + nums[nextIdx] == target:
                    return [startIdx, nextIdx]
                nextIdx += 1
            startIdx += 1

        return []
        

    

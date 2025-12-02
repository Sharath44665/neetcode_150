class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # time: o(N), space: o(N) where N is the length of nums
        result = {}
        for idx in range(len(nums)):
            result[nums[idx]] = idx
        
        counter = 0
        for _ in range(len(nums)+1):
            if counter in result:
                pass
            else:
                return counter
            counter  += 1

# there is a optimal solution using math formula, but i dont do it, because i cant remember that math formula during interview
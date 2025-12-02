class Solution:
    def findMaxConsecutiveOnesTwo(self, nums: List[int]) -> int:
        # time: o(N), space: o(1), where N is the length of arr
        counter = 0
        maxVal = 0
        for val in nums:
            if val == 1:
                counter += 1
            else:
                maxVal = max(maxVal, counter)
                counter = 0

        maxVal = max(maxVal, counter)
        return maxVal

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # time: o(N), space: o(1), where N is the length of arr
        counter = 0
        max = 0
        for val in nums:
            if val == 1:
                counter += 1
            if val == 0 :
                if counter > max:
                    max = counter
                counter = 0
        if counter > max:
            max = counter
        return max
                
        
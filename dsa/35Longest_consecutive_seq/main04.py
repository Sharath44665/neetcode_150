class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time: o(n), space: o(n)
        numSet = set(nums)

        currentLength =0
        maxLength = 0

        for num in numSet:
            if num-1 not in numSet:
                currentLength = 1
                currentNum = num

                #extending to the right
                while currentNum+1 in numSet:
                    currentLength += 1
                    currentNum += 1

                maxLength = max(currentLength, maxLength)

        return maxLength
        

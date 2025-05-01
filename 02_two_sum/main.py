class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # [2, 7, 11, 15], target = 9
        check_num={}
        result = []
        for idx in range(len(nums)):
            val = nums[idx]
            difference = target - val
            if difference in check_num:
                result.append(check_num[difference])
                result.append(idx)
            else:
                if val not in check_num:
                    check_num[val] = idx
        return  result

s = Solution()
nums = [2, 7, 11, 15]
target = 9

nums = [3,2,4]
target = 6
ans = s.twoSum(nums, target)

print(ans)



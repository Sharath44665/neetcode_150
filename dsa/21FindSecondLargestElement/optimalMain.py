def findSecondLargest(nums):
    # time complexity: o(n), space complexity: o(1), where n is the length of nums
    firstLargest = nums[0]
    secondMax = float("-inf")
    for idx in range( len(nums)):
        if nums[idx] > secondMax  and nums[idx] < firstLargest:
            secondMax = nums[idx]
        if nums[idx] > firstLargest:
            secondMax = firstLargest
            firstLargest = nums[idx]

        # if idx == 1 and nums[idx-1] > secondMax and nums[idx-1] < firstLargest: # if second max is the first element
        #     secondMax = nums[idx-1]
            
    return secondMax

nums = [ 55, 32, 97, 45, 32, 88, 21, 97]
# nums = [55, 33]
# nums = [33, 55]
secondMax = findSecondLargest(nums)
print(secondMax)
def partition(nums, low, high):
    pivot = nums[low]
    i = low 
    j = high
    while i< j:
        while nums[i] <= pivot and i < high: 
            i+=1
        while nums[j] >= pivot and j > low:
            j -= 1
        if i< j:
            nums[i],nums[j] = nums[j],nums[i]
    nums[j],nums[low] = nums[low], nums[j]
    return j

def quickSort(nums, low, high):
    # average and best, time complexity: o (n log n), space complexity: o(1) where n is the length of nums
    # worst case time: o(n^2), space : o(1), example nums [2,2,2,2,2,2]
    if low < high:
        partitionIdx = partition(nums, low, high)
        quickSort(nums, low, partitionIdx -1)
        quickSort(nums, partitionIdx+1, high)

nums = [4, 1, 7, 6, 3, 2, 8, 1 ]
quickSort(nums, 0, len(nums)-1)
print(nums)
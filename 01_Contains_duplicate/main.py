def containsDuplicate(nums):
    check_update = {}
    for val in nums: 
        if val in check_update:
            return True
        else:
            check_update[val]= False
    return False

nums = [1,2,3,1,4,2,1]
print(containsDuplicate(nums))



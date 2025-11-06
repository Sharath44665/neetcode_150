def storeFrequencyInDictionary(nums):
    # TC = SC = o(N), where N is nums
    store = {}
    for idx in range(len(nums)): 
        if nums[idx] not in store: # o(1)
            store[nums[idx]] = 1
        else:
            store[nums[idx]] += 1
    return store
    
nums = [5, 6, 7, 1, 9, 1111, 1, 1, 5, 1, 1]

print(storeFrequencyInDictionary(nums))
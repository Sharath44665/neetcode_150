def storeFrequencyInDictionary(nums):
    store = {}
    for idx in range(len(nums)):
        store[nums[idx]] = store.get(nums[idx],0) + 1

    return store

nums = [5, 6, 7, 1, 9, 1111, 1, 1, 5, 1, 1]
print(storeFrequencyInDictionary(nums))
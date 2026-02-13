def insertionSort(arr):
    # arr = [58, 87, 37, 57, 27, 68, 20, 60]
    
    length = len(arr)
    i = 0
    while i < length and i+1 < length:
        left = i
        right = i+1
        while left >= 0 and arr[left] > arr[right]:
            arr[left],arr[right] = arr[right], arr[left]
            left -= 1
            right = left+1
        i += 1
    return arr

arr = [58, 87, 37, 57, 27, 68, 20, 60]
insertionSort(arr)
print(arr)

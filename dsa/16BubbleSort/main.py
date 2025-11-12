# time complexity =  o(n^2), space complexity o(1)
def bubbleSort(a): 
    arrLength = len(a)
    for _ in a:
        i = 0
        j = i+1 
        while i< arrLength and j < arrLength:
            if a[j] < a[i]:
                a[i],a[j] = a[j],a[i] 
            i = i+ 1
            j += 1 
        arrLength -= 1

nums = [5, 8, 1, 6, 9, 2, 4]
bubbleSort(nums) 
print(nums)

def bubbleSortDescending(a):
    arrLength = len(a)
    for _ in a:
        i = 0
        j = i+1 
        while i< arrLength and j < arrLength:
            if a[j] > a[i]:
                a[i],a[j] = a[j],a[i] 
            i = i+ 1
            j += 1 
        arrLength -= 1

nums = [5, 8, 1, 6, 9, 2, 4]
bubbleSortDescending(nums)
print(nums)
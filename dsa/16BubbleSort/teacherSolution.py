# time complexity =  o(n^2), space complexity o(1)
def bubbleSort(a):
    arrLength = len(a)
    for i in range(arrLength-2, -1, -1): # ulta loop
        for j in range(0, i+1):
            if a[j]> a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

nums = [5, 8, 1, 6, 9, 2, 4]
bubbleSort(nums)
print(nums)
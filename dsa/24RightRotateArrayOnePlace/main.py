def rightRotateArrayOnePlace(arr):
    # time complexity o(N), space: o(1), where N is the length of elements
    length = len(arr)
    tempValue = arr[length-1]
    length -= 1
    while length > 0:
        arr[length] =arr[length - 1]
        length -= 1
    arr[0]= tempValue

    pass

arr = [2, 6, 3, 1, 7, 8, 6]
rightRotateArrayOnePlace(arr)
print(arr)
# rightRotateArrayOnePlace(arr)
# print(arr)
# rightRotateArrayOnePlace(arr)
# print(arr)

def rightRotateArrayOnePlaceDemoTwo(arr):
    length= len(arr)
    arr[:] = arr[-1:] + arr[0:length -1] # here arr[:] meaning we didnt used different variable, kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
rightRotateArrayOnePlaceDemoTwo(arr)
print(arr)

def getAllFibonacci(num):
    # time complexity = o(2^n), space complexity = o(2^n), where n = num
    # 0 1 1 2 3 5 8 13 21 ... # fibonacci sequence
    # 0 1 2 3 4 5 6 7  8  ... # num
    if (num == 1 or num == 0):
        return num
    return  getAllFibonacci(num -1) + getAllFibonacci(num-2)
    

ans = getAllFibonacci(8)
print(ans)
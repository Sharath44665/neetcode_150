def printFactors(num):
    # TC = o(N), SC = O(k), where N is the num, k is number factors
    n =1
    result = []
    while n <= num:
        if (num % n == 0):
            result.append(n)
        n += 1
    return result

print(printFactors(20))
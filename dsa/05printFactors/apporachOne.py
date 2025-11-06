def printFactors(num):
    # time complexity = O(N/2) or O(N) , space complexity = o(k)
    # where N is input num, k is the factors
    n = 1
    result = []
    lengthOfLoop = num//2
    while n <= lengthOfLoop:
        if (num%n) == 0:
            result.append(n)
        n += 1
    result.append(num)
    return result

print(printFactors(20))
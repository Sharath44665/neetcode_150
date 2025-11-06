import math
def printFactors(num):
    # TC = o(sqrt(N)), SC = o(k)
    # where N is input num, k is the factors
    lengthOfLoop = math.floor(math.sqrt(num))
    
    result = []
    n = 1
    while n <= lengthOfLoop:
        if (num%n == 0):
            anotherNum = num//n
            result.append(n)
            if (n == anotherNum):
                continue
            result.append(anotherNum)
        n += 1
    return result

print(printFactors(20))

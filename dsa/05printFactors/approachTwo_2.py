import math 
def printFactors(num):
    # TC = o(sqrt(N)), SC = o(k)
    # where N is input num, k is the factors
    lengthOfLoop =  math.floor(math.sqrt(num))
    n = 1
    result = [] 
    while n<= lengthOfLoop:
        if (num%n == 0):
            result.append(n)
            anotherNum = num//n
            if (anotherNum != n):
                result.append(anotherNum)
        n += 1
    # result.sort() o(NLogN)
    return result

print(printFactors(36))
# Using recursion print sum on 1 to N numbers
sum = 0
def getSum(n):
    if n < 0:
        return
    global sum
    sum = sum +n
    getSum(n-1) # not a functional recursion
    return sum

# print(getSum(10))

def getSumTwo(n):
    if n < 0:
        return
    return n + getSum(n-1) # yes, its functional recursion

print(getSumTwo(10))

def getSumTwo(sum, i, n): 
    if n <= 0:
        return sum 
    
    return sum + i + getSumTwo(sum, i+1, n-1) # yes, its functional recursion

ans = getSumTwo(0, 1, 10)
print(ans)


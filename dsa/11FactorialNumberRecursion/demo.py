# using recursion find factorial of number

def findFactorial(n):
    # time complexity o(N), space complexity o(N) where N is the number and space in stack
    if n == 0:
        return 1
    return n * findFactorial(n-1)

ans = findFactorial(5)
print(ans)
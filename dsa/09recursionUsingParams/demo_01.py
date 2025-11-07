# print x, n times using recursion
# explanation: suppose x= 15, n = 3, you should print 15, three times

def printMethod(x, n):
    if n <= 0:
        return
    print(x)
    printMethod(x, n-1)

printMethod(15, 3)

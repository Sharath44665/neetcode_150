# print 1 to N using recursion
counter = 0
def printNumbers(n):
    global counter 
    counter += 1
    if counter > n:
        return
    print(counter) 
    printNumbers(n)

# printNumbers(10)

def printNumbersTwo(i, n):
    print(i)
    i += 1
    if (i > n):
        return
    printNumbersTwo(i, n)

# printNumbersTwo(1, 5)

# same code be written as below 
def printNumbersTwo2(i, n):
    if i > n:
        return
    print(i)
    printNumbersTwo2(i+1, n)

# printNumbersTwo2(1,5)

# using tail recursion 1 to N
def printNumbersThree(i, n):
    if n == i-1:
        return
    printNumbersThree(i, n-1)
    print(n)

# printNumbersThree(1,5)

# using tail recursion N to 1 printing:

def printNumbersThree1(i, n):
    if i>n:
        return
    printNumbersThree1(i+1, n)
    print(i)

printNumbersThree1(1,5)
def printFactors(num):
    n =1
    while n <= num:
        if (num % n == 0):
            print(f"{n}", end=" ")
        n += 1

printFactors(19)
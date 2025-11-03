def armStrongNumber(num):
# time = o (k * log to the base 10 N ) where k is length of number
# space is constant

    # checking the length of number
    n= num
    length = 0
    while  n> 0:
        length += 1
        n = n//10

    n= num 
    sum = 0
    
    while n > 0: # 153
        lastDigit = n%10
        newLength = length
        multiplyResult = 1
        while newLength > 0:
            multiplyResult= multiplyResult * lastDigit
            newLength -= 1
        sum = sum+ multiplyResult
        n = n//10

    if sum == num: 
        print(f"{num} is ArmstrongNumber")
    else:
        print(f"{num} is NOT ArmstrongNumber")
        
# n= 1634
# armStrongNumber(n)

def armStrongNumberTwo(num):
    # o(k) where k is the length of num
    n= num
    length = 0
    while  n> 0:
        length += 1
        n = n//10

    sum =0
    power= length
    while length > 0:
        lastDigit = n % 10
        sum = sum + (lastDigit ** power)
        print(sum)
        length -= 1

    print(sum)


def checkArmStrongNumberThree(num):
    # Time complexity: o(logBase 10 (N)), where N is input Number
    # Space Complexity: o(1)
    n = num
    lengthOfDigit = len(str(n))
    total = 0
    while n > 0:
        lastDigit = n%10 
        total = total + (lastDigit ** lengthOfDigit)
        n = n//10
    return total == num

n= 1634
print(checkArmStrongNumberThree(num=n))


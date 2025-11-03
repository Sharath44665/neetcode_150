n = 1234
# n= 12321
# time complexity o(log_base 10 (N)), where N is number
# Space complexity o(1)
def palindromCheck(num):
    n = num
    result = 0
    prvNum =0
    while n > 0:
        lastDigit = n%10
        result = prvNum *10 + lastDigit
        prvNum = result
        n = n//10

    if result == num:
        print(f"given {num} is palindrome")
    else:
        print(f"given {num} is not palindrome")
    
# palindromCheck(n)

def modifiedCodePalindrome(num):
    n = num
    result = 0

    while n > 0: 
        lastDigit = n % 10
        result = result *10 + lastDigit
        n = n//10
    
    if result == num:
        print(f"{num} is palindrom")
    else:
        print(f"{num} is NOT palindrom")

modifiedCodePalindrome(n)
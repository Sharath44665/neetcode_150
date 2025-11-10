def checkPalindrome(someString):
    # time complexity = o(N), space complexity =o (1), where n is the length of string
    startIdx = 0
    lastIdx = len(someString)-1
    while startIdx < lastIdx:
        if someString[startIdx].lower() != someString[lastIdx].lower():
            return False
        startIdx += 1
        lastIdx -= 1
    return True
    
ans = checkPalindrome("sharath")
print(ans)
ans = checkPalindrome("momOm")
print(ans)

def checkPalindromeRecusion(someString, firstIdx, lastIdx):
    # time complexity = o(N), space complexity =o (N), where n is the length of string
    if someString[firstIdx].lower() != someString[lastIdx].lower():
        return False
    if firstIdx > lastIdx: 
        return True
    return checkPalindromeRecusion(someString, firstIdx + 1, lastIdx - 1)
    
someString = "Sharats"
ans = checkPalindromeRecusion(someString, 0, len(someString)-1)
print(ans)
someString= "momOm"
ans = checkPalindromeRecusion(someString, 0, len(someString)-1)
print(ans)
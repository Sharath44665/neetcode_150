# given two strings 
# s ="azyxyyzaaa"
# q=["d", "a", "y", "x"]
# output: [0, 4, 3, 1] # d repeated 0 times, a repeated 4 times, y repeated 3 times, ... respectively

# to find out how many time q is repeated in s 
# 
# constraints: 
# "a" <= s[i] <= "z"

def findStringOccurence(s,q):
    # time complexity = o(N+M) where n is len(s), m is len(q)
    # space complexity = o(1+l) where l is len(q)
    stringMap={}
    result = []
    for val in s:
        stringMap[val] = stringMap.get(val,0) + 1

    for val in q:
        result.append(stringMap.get(val,0))
    return result
    pass

s ="azyxyyzaaa"
q=["d", "a", "y", "x"]
print(findStringOccurence(s,q))
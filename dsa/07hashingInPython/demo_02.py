# given two arrays 
# n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
# m = [10, 111, 1, 9, 5, 67, 2]
# 
# constraints: 
# 1 <= n[i] <= 10
# n can have 10^8 elements
# m can have 10^8 elements
# 
# need to find how many times elements in m occured in n
# 
# output: [1, 0, 1, 0, 4, 0,  2]
# 
# explanation: 
# 10 occured 1 time 
# 111 occured 0 time 
# 1 occured 1 time 
# 9 occured 0 time 
# 5 occured 4 times
# ... continues

def findOccurence(n, m):
    # time complexity = o(N+M), where N is length of n, M is length of m
    # space complexity = o(k+l), where k is space stored in hashMapN, and l is the space stored in result
    hashMapN = {}
    result = []
    for idx in range(len(n)):
        hashMapN[n[idx]] = hashMapN.get(n[idx], 0) + 1

    for idx in range(len(m)):
        result.append(hashMapN.get(m[idx], 0))
    return result

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

print(findOccurence(n, m))
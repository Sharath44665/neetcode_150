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

# time complexity = o(N+M), where N is length of n, M is length of m
# space complexity = o(1 + k), where k is space stored in result, 1 is stored in hashList
def findOccurence(n, m):
    # from the question, n can have elements between 0, 10, so
    hashList = [0 for _ in range(11)]
    result = []

    for idx in range(len(n)):
        hashList[n[idx]] += 1
    
    for idx in range(len(m)):
        if m[idx] > 10:
            result.append(0)
        else: 
            result.append(hashList[m[idx]])
    return result

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

print(findOccurence(n, m))
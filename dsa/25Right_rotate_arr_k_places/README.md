# Right rotate array k times

https://leetcode.com/problems/rotate-array/?envType=problem-list-v2&envId=two-pointers&difficulty=MEDIUM

hints:

example arr = [1, 2, 3, 4, 5, 6, 7] and k = 3
target arr = [5, 6, 7, 1, 2, 3, 4]

1. first reverse the whole array = [7, 6, 5, 4, 3, 2, 1]

2. now reverse 0 to k-1 = [5, 6, 7, 4, 3, 2, 1]

3. now reverse k to len(arr)-1 = [5, 6, 7, 1, 2, 3, 4] which is our target arr


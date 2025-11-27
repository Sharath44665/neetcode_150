def merge( nums1, m, nums2, n):
        # midx = m - 1
        # nidx = n - 1 
        # right = len(nums1) - 1

        mIdx = m - 1
        nIdx = n - 1
        endIdx = len(nums1) - 1

        # nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        while endIdx >= 0: # [1,2,2,3,5,6]
            if nums2[nIdx] > nums1[mIdx] and nIdx >= 0:
                nums1[endIdx] = nums2[nIdx]
                nIdx -= 1
            else:
                nums1[endIdx] = nums1[mIdx]
                mIdx -= 1
            endIdx -= 1
        print(mIdx)
        print(nIdx)

        # while nidx >= 0:
        #     if midx >= 0 and nums1[midx] > nums2[nidx]:
        #         nums1[right] = nums1[midx]
        #         midx -= 1
        #     else:
        #         nums1[right] = nums2[nidx]
        #         nidx -= 1

        #     right -= 1

# nums1 = [-1, 0, 3, 4, 0, 0, 0, 0]
# m = 4
# nums2 = [0, 2, 3, 5]
# n = 4

nums1 = [2, 3,0]
m = 2
nums2 = [1]
n = 1

# [2,0]

merge(nums1=nums1, m=m, nums2=nums2, n=n)
print(nums1)
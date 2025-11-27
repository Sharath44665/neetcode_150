class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        # time: o(n), space: o(1)
        endIdx = len(nums1) -1
        nidx =  n - 1
        midx = m - 1

        while endIdx >=0:
            if midx <= -1: # this code if [2, 3, 4, 0], [1] put, everything to left, edge case
                nums1[endIdx] = nums2[nidx]
                nidx -= 1
            elif nidx >= 0 and nums2[nidx] > nums1[midx]:
                nums1[endIdx] = nums2[nidx]
                nidx -= 1
            else:
                nums1[endIdx] = nums1[midx]
                midx -= 1
            endIdx -= 1
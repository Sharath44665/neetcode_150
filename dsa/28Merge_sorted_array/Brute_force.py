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
        # [1, 2, 3, 4, 0, 0, 0, 0], [2, 2, 5, 6]
        # time: o(n * m) space: o(1)
        i = j = 0
        k = m
        while i< len(nums1) and j < n: #[1, 2, 2, 3, 4] k=2
            if nums1[i] <= nums2[j] and i < m:
                i += 1
            elif nums2[j] < nums1[i]:
                # shift right by one
                while k > i: 
                    nums1[k] = nums1[k - 1] 
                    k -= 1
                nums1[i] = nums2[j]
                # i += 1
                m += 1
                k = m
                j += 1 
            elif i >= m:
                nums1[i] = nums2[j]
                i += 1
                j += 1
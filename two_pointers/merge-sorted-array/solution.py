class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Combine nums1 and nums2
        nums1[m:] = nums2[:n]
        """
        nums1[:] = [nums for nums in nums1 if nums!=0]
        """
        # Sort the merged list in-place
        nums1.sort()


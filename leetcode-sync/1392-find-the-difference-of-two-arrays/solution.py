class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result_nums1 =[]
        result_nums2 =[]
        
        for num in nums1:
            if num not in nums2:
                result_nums1.append(num)
                
        result_nums1 = list(set(result_nums1))
        
        for num in nums2:
            if num not in nums1:
                result_nums2.append(num)
        result_nums2 = list(set(result_nums2))
                
        return [result_nums1] + [result_nums2]

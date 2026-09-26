class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Handle the edge case of an empty list

        k = 1
        i = 1
        
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                if k != i:
                    nums[k] = nums[i]
                k += 1
            i += 1
        
        return k


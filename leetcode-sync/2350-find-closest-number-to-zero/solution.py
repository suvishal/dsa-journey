class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        s = nums[0] #s is shortest distance or the closest number
        for i in nums:
            if abs(i) < abs(s):
                s = i
        
        if s < 0 and abs(s) in nums:
            return abs(s)
        else:
            return s

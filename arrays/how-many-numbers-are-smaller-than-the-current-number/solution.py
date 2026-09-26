class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            c = 0 
            
            for j in range(len(nums)):
                if nums[i] > nums[j] and  j != i :
                    c += 1
                j += 1
            ans.append(c)
            
            
        return ans
            
        

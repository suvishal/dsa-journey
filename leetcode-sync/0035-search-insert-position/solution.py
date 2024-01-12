class Solution:

  def searchInsert(self, nums, target):
    
    for i in range(len(nums)):
    
      if nums[i] == target:
        return i
        
    for i in range(len(nums)):   

      if nums[i] > target:
        return i
      
      if i == len(nums) - 1:
        return len(nums)

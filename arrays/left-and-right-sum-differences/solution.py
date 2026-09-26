class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = [0]
        rightsum = [0]
        ans = []
        for i in range(1, len(nums)):
             leftsum.append(leftsum[-1] + nums[i - 1])
           
        nums.reverse()
        for j in range(1, len(nums)):
             rightsum.append(rightsum[-1] + nums[j - 1])

        rightsum.reverse()
        for i in range(len(nums)):
            ans.append(abs(leftsum[i]-rightsum[i]))
        
        return ans


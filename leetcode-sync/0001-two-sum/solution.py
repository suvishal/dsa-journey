class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)-1):
            for j in range(len(nums)):
                if i < j and nums[i] + nums[j] == target: 
                    ans.append([i,j])
        return ans[0]

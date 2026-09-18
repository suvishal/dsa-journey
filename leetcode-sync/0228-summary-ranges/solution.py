class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        s = []
        i = 0
        while i < len(nums):
            start = nums[i]

            while i < len(nums)-1 and nums[i+1]-nums[i]==1:
                i += 1
                
            if start != nums[i]:
                    s.append(str(start)+ '->'+ str(nums[i]))
            else:
                s.append(str(nums[i]))

            i += 1

        return s

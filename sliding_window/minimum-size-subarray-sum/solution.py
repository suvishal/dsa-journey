class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j, window_sum = 0, 0, 0
        min_length = float('inf')
        
        while j < len(nums):
            window_sum += nums[j]

            while window_sum >= target :
                window_sum -= nums[i] 
                min_length = min(j-i+1, min_length)

                i += 1
            
            j += 1

        if min_length == float('inf'):
            return 0
        else:
            return min_length

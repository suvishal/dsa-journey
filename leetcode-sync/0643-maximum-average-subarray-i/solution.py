class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i,j,window_sum = 0,0,0
        max_avg = float('-inf')
        for j in range(len(nums)):
            window_sum += nums[j]

            if j-i+1 < k:
                j += 1
            elif j - i + 1 == k:
                max_avg = max(max_avg,window_sum/k)
                window_sum -= nums[i]
                i += 1
                j += 1
        
        return max_avg




class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        left = 0 
4        right = len(numbers)-1
5
6        while left < right:
7        
8            if numbers[left]+numbers[right] == target:
9                return [left+1,right+1]
10            elif target > numbers[left] + numbers[right]:
11                left += 1
12            elif target < numbers[left] + numbers[right]:
13                right -= 1

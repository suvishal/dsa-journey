class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1
        first = -1
       
        while i <= j :
            mid = (i + j)//2
            if  nums[mid] == target:
                first = mid
                j = mid - 1
            elif target > nums[mid] :
                i = mid + 1
            else:
                j = mid - 1

        i, j = 0, len(nums)-1
        last = -1

        while i <= j :
            mid = (i + j)//2
            if  nums[mid] == target:
                last = mid
                i = mid + 1
            elif target > nums[mid] :
                i = mid + 1
            else:
                j = mid - 1
            

        return [first,last]



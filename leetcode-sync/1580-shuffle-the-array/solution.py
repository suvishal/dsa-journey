class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = nums[:n]
        b = nums[n:]
        ans = []
        j,k = 0,0
        for i in range(2*n):
            if i % 2 == 0:
                ans.append(a[j])
                j += 1
            else :
                ans.append(b[k])
                k += 1
    
        return ans
        

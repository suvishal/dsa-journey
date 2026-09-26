class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        i = 0
        ans = []
        a = max(candies) - extraCandies
        while i < (len(candies)):
            if candies[i] >= a:
                ans.append(True)
            else :
                ans.append(False)
            i += 1
        return ans
        

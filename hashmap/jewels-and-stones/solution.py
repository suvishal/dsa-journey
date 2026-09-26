class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0 
        s = set(jewels)

        for stone in stones:
            if stone in s:
                c += 1
        
        return c

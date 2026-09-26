class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = max(1, (sum(piles) + h - 1) // h)
        right = max(piles)

        while left <= right:
            mid = left + (right - left) // 2
            total_hours = 0

            for pile in piles:
                total_hours += (pile + mid - 1) // mid
                if total_hours > h:   # early exit
                    break

            if total_hours <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left

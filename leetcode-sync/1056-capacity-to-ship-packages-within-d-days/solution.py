class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i = max(weights)
        j = sum(weights)
        ans = j
        while i <= j :
            mid = i + (j-i) // 2
            

            current_load = 0
            total_days = 1

            for weight in weights:
                if current_load + weight > mid:
                    total_days += 1
                    current_load = weight
                else:
                    current_load += weight

            if total_days <= days:
                ans = mid
                j = mid - 1
            else:
                i = mid + 1

        return i

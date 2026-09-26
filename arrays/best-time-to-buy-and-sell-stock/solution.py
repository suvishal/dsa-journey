class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrices = float('inf')
        maxProfit = 0
        for price in prices:
            if price < minPrices :
                minPrices = price
            else :
                maxProfit = max(maxProfit, price - minPrices)
        return maxProfit

            

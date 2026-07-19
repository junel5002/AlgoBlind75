class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        maxPrice = 0
        
        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maxPrice = max(maxPrice, profit)
            else:
                L = R
            R += 1
        return maxPrice
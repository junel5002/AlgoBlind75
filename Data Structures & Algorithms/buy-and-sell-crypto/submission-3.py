class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        max_profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit
                
                  
        
    
    #NB:First we start with the buying and selling pointers and we go through the prices and calculate the profit when selling prices is higher so we update the buying day if price lowers and finally return the highest profit.
'''
prices = [10,2,5,1,7,1]
                 ^  
                 ^

max = 0

4 = current max
max = max(currentmax, max)

    not optimised
    have a nested loop
    i ith..
    and j start at i+1 
    comapre check the difference
    have max to track 
    return max

prices[0] = 10>> first day
output: 6

bascially two pointers/sliding technique alrgotim
left pointer starts/ checl the price of the neetcoin on the ith day
right check for a day we can sell it

if there's a profit 


in the case where the right pointer exceeds the array length; we stop the lop
while lop



'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        max_profit = 0
        n = len(prices)-1 


        while r <= n:

            if prices[r] > prices[l]:
                current_max = prices[r] - prices[l]

                max_profit = max(current_max, max_profit)
            else:
                l = r

            r += 1

        return max_profit
        
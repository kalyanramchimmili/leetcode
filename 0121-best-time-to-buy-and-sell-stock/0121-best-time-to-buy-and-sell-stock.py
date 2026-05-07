"""
1. min value as first int, profit as 0
2. find the min value of the list and record it
3. find the max value by sub current prices[i]-min value and record it
4. after iteration return profit

timecomp:- O(n)
space:- O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        min_value = prices[0]
        
        for i in range(n):
            min_value = min(min_value, prices[i])
            profit = max(profit, prices[i]-min_value)
        
        return profit

        



        
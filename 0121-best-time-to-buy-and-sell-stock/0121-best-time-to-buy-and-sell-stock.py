class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        min_value = prices[0]
        
        for i in range(n):
            min_value = min(min_value, prices[i])
            profit = max(profit, prices[i]-min_value)
        
        return profit

        



        
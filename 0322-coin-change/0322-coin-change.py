class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for currAmount in range(1, amount+1):
                if currAmount >= coin:
                    dp[currAmount] = min(dp[currAmount], 1+dp[currAmount-coin])
        if dp[amount] != float('inf'):
            return dp[amount]
        return -1
        
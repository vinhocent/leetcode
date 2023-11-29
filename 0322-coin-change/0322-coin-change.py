class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float(inf)] * (amount + 1)
        for i in range(amount + 1):
            if i == 0:
                dp[0] = 0
            else:
                for coin in coins:
                    if i - coin >= 0:
                        dp[i] = min(dp[i - coin] + 1, dp[i])

            
        return dp[amount] if dp[amount] != float(inf) else -1
                        
            
#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #Solution 1: 1D-Array
        
        dp = [float("inf") for x in range(amount + 1)]
        
        dp[0] = 0
        
        for q in range(0, len(coins)):
            for a in range(1, amount + 1):
                if (coins[q] <= a):
                    
                    dp[a]= min(dp[a-coins[q]] + 1 , 
                                 dp[a])
                    
        answer = dp[amount]

        return answer if answer != float("inf") else -1



        # Solution 2: 2D-Array        
        # dp = [[float("inf") for x in range(len(coins))] for x in range(amount + 1)]
        
        # for a in range((len(coins))):
        #     dp[0][a] = 0
        
        # for q in range(0, len(coins)):
        #     for a in range(1, amount + 1):
        #         if (coins[q] >a):
        #             dp[a][q]=dp[a][q-1]
        #         else:
                    
        #             dp[a][q]= min(dp[a-coins[q]][q] + 1 , 
        #                          dp[a][q-1])
                    
        # answer = dp[amount][len(coins) - 1]

        # return answer if answer != float("inf") else -1
        
# @lc code=end


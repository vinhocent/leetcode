#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        maxprofit = 0 
        soldyet = False 
        for i in range(1, len(prices)):
            if (prices[i] - prices[i-1]) > 0 :
                maxprofit += (prices[i] - prices[i-1])
                
        return maxprofit
        
        
# @lc code=end


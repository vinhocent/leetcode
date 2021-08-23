#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minbuy = prices[0]
        maxprofit = 0 
        soldyet = False 
        for i in range(0, len(prices)):
            if (prices[i] < minbuy) :
                minbuy = prices[i]
            elif (prices[i] - minbuy ) > maxprofit:
                maxprofit = prices[i] - minbuy
                
        return maxprofit
        
        
# @lc code=end


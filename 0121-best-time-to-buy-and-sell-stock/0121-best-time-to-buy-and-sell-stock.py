class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        i = 0
        j = 1
        
        minbuy = 0 
        while j < len(prices):
            if prices[i] > prices[j]:
                i+= 1
            else:
                minbuy = prices[i]
                maxprofit = max(prices[j]-minbuy, maxprofit)
                j+= 1
                
                
        return maxprofit
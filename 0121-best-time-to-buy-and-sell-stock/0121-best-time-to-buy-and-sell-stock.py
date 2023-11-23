class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumprofit = 0 
        
        i = 0
        
        j=0
        
        while (j < len(prices)):
            if prices[i] > prices[j] :# if stock goes down
                i+= 1
                
            else:
            
                maximumprofit = max(maximumprofit, prices[j]-prices[i])
                print(f"{maximumprofit} {i} {j}")
                j+=1

        return maximumprofit
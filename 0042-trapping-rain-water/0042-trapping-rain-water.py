class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftmax = [0] * len(height)
        leftmax[0] = height[0]
        
        for i in range(1,len(height)):
            leftmax[i] = max(leftmax[i-1], height[i])
            
        rightmax = [0] * len(height)
        rightmax[len(height) - 1] = height[len(height)-1]
    
        for i in range(len(height)-2, 0 , -1):
            rightmax[i] = max(rightmax[i+1], height[i])
            
        totalWater = 0
        
        
        for i in range(1,len(height)): 
            mincurr = min(leftmax[i],rightmax[i])
            totalWater += max(mincurr - height[i], 0)
            
        return totalWater
        
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        maxx = 0
        minheight = 0
        while( l < r):
            minheight = max(minheight, min(height[l],height[r]) )

            area = min(height[l],height[r]) * ( r - l )
            maxx = max(area, maxx)
            
            
    
            if ( height[l ] < height[r]):
                l = l + 1
            else:
                r = r - 1
                
            print(l)
            print(r)
                
        return maxx         
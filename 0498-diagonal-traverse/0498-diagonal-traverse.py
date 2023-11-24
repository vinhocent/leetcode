class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        
        # 1 2 3 
        # 4 5 6
        # 7 8 9
        
        # if its even go reverse order
        
        n = len(mat[0])
        m = len(mat)
        
        up = True
        col = 0
        row = 0
        ans = []
        while col < n and row < m:
            print(f"{row} {col} {up}")
            
            if up == True:
                
                
                while row > 0 and col < n - 1:
                    ans.append(mat[row][col])

                    row -= 1
                    col += 1
                    
                
                ans.append(mat[row][col])    
                if col == n-1:
                    row += 1
                    
                else:
                    col += 1
                    
                    
            else:
                
                while col > 0 and row < m - 1:
                    ans.append(mat[row][col])

                    row += 1
                    col -= 1
                    
                
                ans.append(mat[row][col])   
                
                if row == m-1:
                    col += 1
                    
                else:
                    row += 1
                    
            up = not up
            
        return ans
                    
                    
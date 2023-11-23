class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        
                
        i = 0 
        
        maximumfruits = 0 
        currcount = 0
        
        fruitdict = defaultdict(int)
                
        for j in range(0, len(fruits)):
            
            fruitdict[fruits[j]] += 1 # should keep track of num of fruits
            
         

            
            
            while len(fruitdict) > 2 :
                
                fruitdict[fruits[i]] -= 1

                if fruitdict[fruits[i]] == 0:
                    fruitdict.pop(fruits[i])
                    
                i += 1
            currcount = j - i + 1
            
            maximumfruits = max(currcount,maximumfruits)
            
            
        return maximumfruits
            
            
            
            
            
            
            
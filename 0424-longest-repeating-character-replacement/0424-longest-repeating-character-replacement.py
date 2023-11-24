class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       
        i,j = 0 , 0
        dict = defaultdict(int)
        maxchar = s[0]
        maxlen = 0
        currlen = 0
        
        while j < len(s):
            
            
            dict[s[j]] = 1 + dict.get(s[j], 0)
            
        

                
            while ((j - i + 1 - max(dict.values())) > k):
                dict[s[i]] -= 1
                i += 1
            maxlen = max(maxlen, j - i + 1)

            j += 1

                
        return maxlen
                
                
                
            
                
            
            
            
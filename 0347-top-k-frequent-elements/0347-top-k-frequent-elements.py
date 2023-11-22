class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        
        
        for i in nums:
            if i not in dict:
                dict[i] = 1
                
            else:
                dict[i] += 1
            

        sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
        sorted_x.reverse()
        maxlist = []
        j = 0
        for i in sorted_x:
  
            if k == j:
                break
            maxlist.append(i[0])
            j += 1
            
                
        return maxlist
            
            
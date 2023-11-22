class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        retarr = [[] for i in range(len(strs))]
        strcopy = strs.copy()
        
        for i ,c in enumerate(strcopy):
            strcopy[i]=''.join(sorted(c))
            
        dict = {}
        for i , c in enumerate(strcopy):
            # print(retarr)

            if c not in dict:

                dict[c] = i
                # print(i)
                retarr[i].append(strs[i])
            else:
                retarr[dict[c]].append(strs[i])
        realarray = []
        for i,c in enumerate(retarr):

            if len(c) != 0:
                realarray.append(c)
                
        return realarray
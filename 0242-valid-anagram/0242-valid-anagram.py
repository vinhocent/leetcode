class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        if len(s) !=len(t):
            return False
        dictS = {}
        dictT = {}
        
        
        for i , c in enumerate(s):
            if (c not in dictS):
                 dictS[c] = 1
            else:
                dictS[c] +=1
                
            if (t[i] not in dictT):
                dictT[t[i]] = 1
            else:
                dictT[t[i]] += 1
                
                
        # // dictionary with all the ascii characters
        for i in dictS:
            if i not in dictT:
                return False
            if dictS[i] != dictT[i]:
                return False
        
            
            
        return True
        
        
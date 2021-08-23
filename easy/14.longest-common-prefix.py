#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        same = True
        
        for i in (range (1, len(strs))): 
            answer = ""
            minlen = min(len(strs[i]), len(strs[0]))
            
            minstring = min(strs[i], strs[0])
            for k in range(minlen):
                if (strs[i][k] == strs[0][k]):
                    answer += minstring[k]
                else:
                    break
            strs[0] = answer
                      
        return strs[0]
                    
        
# @lc code=end


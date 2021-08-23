#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlength = 0
        dict = {}
        i=0
        dellen= 0 
        
        if (len(s) ==  1):
            return 1
        
        while ( i < len(s)):

            if not (s[i] in dict):
                dict[s[i]] = s[i]
                i += 1
                maxlength = max(i - dellen, maxlength)
            else:
                del dict[s[dellen]]
                dellen += 1
            
            
        return maxlength
        
# @lc code=end


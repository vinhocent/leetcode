#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        a = ""
        
        s = lower(s)
        
        for i in (range(len(s))):
            if (57 >= ord(s[i]) >= 48) or (122  >= ord(s[i]) >= 97) :
        
                a += (s[i])  
            
        print(a)
                
        a = lower(a)
            
        return (a == a [:: -1])
        
# @lc code=end


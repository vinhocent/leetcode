#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0 :
            return False
        else:
            original = x
            
            answer = 0            
        
            while x > 0 :
                answer = (x % 10) + (answer * 10)
                x  /=  10

            return True if (original == answer) else False
        
# @lc code=end


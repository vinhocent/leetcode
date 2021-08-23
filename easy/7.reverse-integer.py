#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = 0
        neg = False
        if x < 0:
            x *= -1 
            neg = True
        
        while x > 0 :
             answer = (x % 10) + (answer * 10)
             x  /=  10
        
        
        return 0 if answer > 2147483647  else ((answer * -1) if neg else answer)
        
# @lc code=end


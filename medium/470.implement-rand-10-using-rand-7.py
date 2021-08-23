#
# @lc app=leetcode id=470 lang=python
#
# [470] Implement Rand10() Using Rand7()
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        num1 = rand7()
        num2 = rand7() 
        
        while (num1) > 5:
            num1 = rand7()
            
        while (num2) == 7:
            num2 = rand7()
 
            
        return num1 + 5 if num2 >3 else num1
        
# @lc code=end


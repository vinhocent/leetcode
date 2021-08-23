#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        dict = {"(" : ")" , "{" : "}" , "[" : "]"}
        array =[]
        for x in s:
            if x in dict.keys():
                array.append(x)
            elif (len(array) == 0) or (x != dict[array[-1]]):
                return False
            elif (x == dict[array[-1]]):
                array.pop()
        return (len(array) == 0)    
        
# @lc code=end


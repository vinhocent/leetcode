#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        for v in reversed(s):
            if v.isspace():
                if cnt: break
            else: cnt += 1
        return cnt
        
# @lc code=end


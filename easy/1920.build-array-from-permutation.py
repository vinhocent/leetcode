#
# @lc app=leetcode id=1920 lang=python
#
# [1920] Build Array from Permutation
#

# @lc code=start
class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


        #todo: do this in o(1) space
        array = [] 
        
        for i in range(len(nums)):
            array.append(nums[nums[i]])         
        return array
        
# @lc code=end


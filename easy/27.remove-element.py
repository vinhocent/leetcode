#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        placeint = 0        
        for i in range(0 , len(nums)):
            if (nums[i] != val):   
                nums[placeint] = nums[i]
                placeint += 1    
        return placeint 
        
# @lc code=end


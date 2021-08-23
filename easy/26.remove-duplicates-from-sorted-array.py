#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        placeint = 0
        
        for i in range(1 , len(nums)):
            if (nums[i] != nums[placeint]):
                placeint += 1
                nums[placeint] = nums[i]
    
        return placeint + 1
        
# @lc code=end


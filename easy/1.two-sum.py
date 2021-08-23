#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for idx in range(0, len(nums)):
            if not((target - nums[idx]) in dict) :
                dict[nums[idx]] = idx
            else: 
                return (idx, dict[(target - nums[idx])])
                
# @lc code=end


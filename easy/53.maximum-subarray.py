#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = - float("inf")
        
       
        
        
        pre= [0 for x in range(len(nums) + 1)]

        if (len(nums) == 1):
            return nums[0]
        for i in range(1, len(nums) + 1):
            pre[i] = (pre[i-1]+nums[i - 1])
       
        minpre = pre[0]
    
        for i in range(1, (len(nums)+ 1)):
            answer = max (answer, pre[i] - minpre)
            minpre = min(minpre, pre[i])
            
        return answer
                
        
# @lc code=end


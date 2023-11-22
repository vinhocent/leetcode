class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        # given a number , we know how much we should add to get to our target
        
        
        dict = {}
        
        for i , c in enumerate(nums):
            
            if target - c not in dict:
                dict[c] = i
                
            else: 
                return i, dict[target-c]
        
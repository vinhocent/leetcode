#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1 , -1):            
            if i == 0 and (digits[i] + 1 == 10):
                digits[i] = 0
                digits.insert(0,1)                
                return digits  
            elif digits[i] + 1  < 10:  
                digits[i] += 1                
                return digits           
            else:
                digits[i] = 0

        # solution 2: 

        # if (digits[-1] + 1 < 10):
        #     digits[-1] += 1
        #     return digits
        
        # for i in range(len(digits) - 1, -1 , -1):
        #     print i
            
        #     if i == 0 and (digits[i] + 1 == 10):
        #         digits[i] = 0
        #         digits.insert(0,1)
                
        #         return digits
            
            
        #     elif digits[i] + 1  < 10:
                
        #         digits[i] += 1
                
        #         return digits
            
        #     else:
        #         print digits[i] + 1
        #         digits[i] = 0
        #         print digits[i]    
        
# @lc code=end


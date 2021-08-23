#
# @lc app=leetcode id=412 lang=python
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        array = [0 for x in range(n)]
        for i in range(1,n + 1):
            print(i)
            if i % 3 == 0 and i % 5 == 0:
                
                array[i - 1 ] = "FizzBuzz"
                
            elif i % 3 == 0:
                array[i - 1 ] = "Fizz"
                
            elif i % 5 == 0:
                array[i - 1 ] = "Buzz"
                
            else:
                array[i - 1] = str(i)
                 
        return array
        
# @lc code=end


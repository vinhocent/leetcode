#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        subc = 0
        subx = 0
        subi = 0
        ans = 0
        
        dict = {"I" : 1 , "V" : 5 , "X" : 10 , "L" : 50 ,"C" : 100 ,"D" : 500 ,"M" : 1000 }
        for inner in ["CD", "CM"]:
            
            subc += s.count(inner)
            if inner == "CD":
                s = s.replace(inner, "D")
            if inner == "CM":
                s = s.replace(inner, "M")
            
            
        for inner in ["XL", "XC"]:
            subx += s.count(inner)
            if inner == "XC":
                s = s.replace(inner, "C")
            if inner == "XL":
                s = s.replace(inner, "L")

        
        for inner in ["IV", "IX"]:
            subi += s.count(inner)
            if inner == "IX":
                s = s.replace(inner, "X")
            if inner == "IV":
                s = s.replace(inner, "V")
            
        for i in s:
            ans += dict[i]
            

        
        for k in range(0, subc):
            ans -= 100
        
        for k in range(0, subx):
            ans -= 10
            
        for k in range(0, subi):
            ans -= 1
            
        return ans
        
# @lc code=end


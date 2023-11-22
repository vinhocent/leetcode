class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.replace(" ", "")
        s=s.lower()
        s='.'.join(c for c in s if c.isalnum())
        print(s)
        
        i = 0
        j = len(s) - 1
        if (len(s) == 0 ):
            return True

        
        while i != j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

            
        return True
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        i = 0 
        j = 0

        dict = {}

        currlen = 0
        maxlen = 0
        
        if len(s) == 1:
            return 1

        while j < len(s):

            if s[j] not in dict:
                dict[s[j]] = j
                j+=1
                maxlen = max(j - i, maxlen)


            else:

                del dict[s[i]]
                i+=1

        return maxlen

        
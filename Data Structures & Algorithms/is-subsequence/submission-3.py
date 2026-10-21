class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        if len(s) > 0 and len(t) == 0:
            return False
        
        #if len()

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            
           # elif j == len(t) - 1:
            #    return False
            
            else:
                j += 1
        
        return i == len(s)
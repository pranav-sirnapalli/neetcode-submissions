class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        s = s[::-1]

        length = 0

        i = 0
        while s[i] == " ":
            i += 1
        
        while s[i] != ' ':
            length += 1
            i += 1
        return length

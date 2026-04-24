class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumstr = ''
        for i in s:
            if ord(i) in range(48, 58) or ord(i) in range(65, 90) or ord(i) in range(97, 123):
                alphanumstr = alphanumstr + i
        alphanumstr = alphanumstr.lower()
        alphanumstrrev = alphanumstr[::-1]
        
        if alphanumstrrev == alphanumstr:
            return True
        else:
            return False
        
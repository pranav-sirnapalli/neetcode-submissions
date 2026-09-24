class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_curr = ""
        for i in s:
            if i.isalnum():
                s_curr = s_curr + i
        s_curr = s_curr.lower()
        s_curr_rev = s_curr[::-1]
        return s_curr_rev == s_curr

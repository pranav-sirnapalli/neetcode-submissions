class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        x_copy = x

        while x_copy > 0:
            res = (res*10) + (x_copy % 10)
            x_copy = x_copy // 10
        return res == x
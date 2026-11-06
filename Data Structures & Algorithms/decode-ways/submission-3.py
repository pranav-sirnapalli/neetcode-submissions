class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dp(i):
            if i == len(s):
                return 1
            
            elif s[i] == "0":
                return 0
            
            elif i in memo:
                return memo[i]
            
            else:
                val = dp(i+1)
                if i + 1 < len(s):
                    if s[i] == "1" or (s[i] == "2" and s[i+1] <= "6"):
                        val += dp(i+2)
                memo[i] = val
                return memo[i]

        return dp(0)
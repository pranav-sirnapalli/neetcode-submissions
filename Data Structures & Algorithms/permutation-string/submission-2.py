class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        p = [0] * 26
        q = [0] * 26

        if n > m:
            return False

        for ch in s1:
            p[ord(ch) - ord('a')] += 1
        
        for ch in s2[:n]:
            q[ord(ch) - ord('a')] += 1
        
        if p == q:
            return True
        
        for i in range(n, m):
            q[ord(s2[i]) - ord('a')] += 1
            q[ord(s2[i-n]) - ord('a')] -= 1
            if p == q:
                return True
        return False
        
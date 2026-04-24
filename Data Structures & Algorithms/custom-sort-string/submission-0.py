from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        res = []

        for c in order:
            if c in freq:
                res.append(c * freq[c])
                del freq[c]
        
        for c, cnt in freq.items():
            res.append(c * cnt)
        return "".join(res)
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        res = []
        matched = {']': '[', '}': '{', ')': '('}
        left_val = {'[', '{', '('}

        for i in s:
            if i in left_val:
                res.append(i)
            else:
                if not res or res[-1] != matched[i]:
                    return False
                res.pop()
        
        if len(res) == 0:
            return True
        else:
            return False
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(startidx, endidx):
            if startidx == endidx == n:
                res.append("".join(stack))
                return
            
            if startidx < n:
                stack.append("(")
                backtrack(startidx + 1, endidx)
                stack.pop()
            
            if endidx < startidx:
                stack.append(")")
                backtrack(startidx, endidx + 1)
                stack.pop()

        backtrack(0, 0)
        return res
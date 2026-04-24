from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        operators = ['+', '-', '*', '/']
        d = deque()
        res = 0
        val1 = 0
        val2 = 0

        for i in tokens:
            if i not in operators:
                d.appendleft(int(i))
            else:
                val1 = d.popleft()
                val2 = d.popleft()
                if i == '+':
                    val1 = val1 + val2
                if i == '*':
                    val1 = val1 * val2
                if i == '-':
                    val1 = val2 - val1
                if i == '/':
                    val1 = int(val2 / val1)
                d.appendleft(val1)
        return val1
            





        
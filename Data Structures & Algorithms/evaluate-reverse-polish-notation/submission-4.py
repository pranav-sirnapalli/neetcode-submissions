from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        operators = {'+', '-', '*', '/'}
        val1 = 0
        val2 = 0
        d = deque()

        for i in tokens:
            if i not in operators:
                d.appendleft(int(i))
            else:
                val1 = d.popleft()
                val2 = d.popleft()
                if i == '+':
                    val2 = val2 + val1
                if i == '-':
                    val2 = val2 - val1
                if i == '*':
                    val2 = val2 * val1
                if i == '/':
                    val2 = int(val2/val1)
                d.appendleft(val2)
        return val2



        
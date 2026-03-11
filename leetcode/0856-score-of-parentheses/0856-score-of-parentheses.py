class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        nums = []
        ans = 0
        for i in s:
            if i == "(":
                stack.append(i)
            elif i == ")":
                x = 0 
                while isinstance(stack[-1], int):
                    x += stack.pop()
                if x:
                    stack.pop()
                    stack.append(x * 2)
                else:
                    stack.pop()
                    stack.append(1)

        return sum(stack)
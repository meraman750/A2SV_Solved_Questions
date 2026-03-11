class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        temp = ""
        num = ""

        for i in range(len(s)):
            if s[i].isdigit():
                num += s[i]

            elif s[i] == "[":
                if temp:
                    stack.append(temp)
                    temp = ""
                stack.append(int(num))
                num = ""

            elif s[i].isalpha():
                temp += s[i]

            elif s[i] == "]":
                if temp:
                    stack.append(temp)
                    temp = ""

                txt = stack.pop()

                while stack and isinstance(stack[-1], str):
                    txt = stack.pop() + txt

                n = stack.pop()
                ans = txt * n
                f = ""

                if stack and isinstance(stack[-1], str):
                    f = stack.pop()

                stack.append(f + ans)

        if temp:
            stack.append(temp)

        return "".join(stack)
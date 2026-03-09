class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {")":"(", "}":"{", "]":"["}
        # if len(s) % 2 == 1:
        #     return False
        for i in s:
            if i in my_dict.values():
                stack.append(i)
            elif stack: 
                if stack[-1] != my_dict[i]:
                    return False
                else:
                    stack.pop()
            elif not stack:
                return False
        if stack:
            return False    
        return True


        # for n in s:
        #     if n in my_dict.values():
        #         stack.append(n)
        #     elif n in my_dict.keys() and (len(stack)==0 or stack.pop() != my_dict[n]):
        #         return False
        # return True
                
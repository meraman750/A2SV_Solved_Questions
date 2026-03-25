class Solution:
    def splitString(self, s: str) -> bool:
        temp = []
        def back(l):
            if l >= len(s):
                for i in range(1, len(temp)):
                    if temp[i-1] - temp[i] != 1:
                        return False
                if len(temp) > 1:
                    return True
                else:
                    return False
                 
            
            for i in range(l, len(s)):
                temp.append(int(s[l:i+1]))
                if back(i+1):
                    return True
                temp.pop()
            return False

        return back(0)


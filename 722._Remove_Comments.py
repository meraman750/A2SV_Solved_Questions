class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []

        flag = True
        temp = ""
        for s in source:
            i = 0
            while i < len(s):
                if flag and i+1 < len(s) and s[i] == "/" and s[i+1] == "*":
                    i+=2
                    flag = False
                    continue
                if not flag and s[i] == "*" and s[i+1] == "/":
                    flag = True 
                    i+=2
                    continue
                if flag and i+1 < len(s) and s[i] == "/" and s[i+1] == "/":
                    break
                if flag:
                    temp += s[i]
                i+=1
            if temp and flag:
                ans.append(temp)
                temp = ""
        return ans

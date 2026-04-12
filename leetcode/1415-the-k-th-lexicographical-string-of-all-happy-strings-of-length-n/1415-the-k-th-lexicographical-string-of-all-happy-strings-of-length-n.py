class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        temp = []
        mp = ["a", "b", "c"]
        def calc():
            if len(temp) == n:
                ans.append("".join(temp[:]))
                return 
            for i in range(len(mp)):
                if temp and temp[-1] == mp[i]:
                    continue
                temp.append(mp[i])
                calc()
                temp.pop()
        calc()
        # print(ans)
        ans.sort()
        return ans[k-1] if k <= len(ans) else ""

            
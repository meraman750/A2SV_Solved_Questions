class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        res = []
        def calc(n):
            if n >= len(pattern):
                res.append("".join(map(str, ans[:])))
                return 

            if pattern[n] == "I":
                for i in range(ans[-1]+1, 10):
                    if i not in set(ans):
                        ans.append(i)
                        calc(n+1)
                        ans.pop()
            else:
                for i in range(1, ans[-1]):
                    if i not in set(ans):
                        ans.append(i)
                        calc(n+1)
                        ans.pop()

        for i in range(1, 10):
            ans.append(i)
            calc(0)
            ans.pop()
        res.sort()
        return res[0]
        

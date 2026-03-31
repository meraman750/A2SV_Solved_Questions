class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = [0] * k
        minn = float("inf")

        def calc(n, ans):
            nonlocal minn
            if n >= len(cookies):
                minn = min(minn, max(ans))
                return 

            if max(ans) > minn:
                return 

            for j in range(k):
                ans[j] += cookies[n]
                calc(n+1, ans)
                ans[j] -= cookies[n]

        calc(0, ans)
        return minn


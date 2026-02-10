class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [""] * len(s)

        for j in range(len(s)):
            ans[indices[j]] = s[j]
        return "".join(ans)
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)

        ans = 0
        for key, val in count_s.items():
            if key in count_t:
                if val >= count_t[key]:
                    ans += val - count_t[key]
            else:
                ans += val

        return ans
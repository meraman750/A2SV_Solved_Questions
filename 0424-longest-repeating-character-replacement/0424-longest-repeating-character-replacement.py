class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        n = len(s)
        max_count = 0
        ans = 0
        l = 0
        for i in range(n):
            count[s[i]] = count.get(s[i], 0) +1
            max_count = max(max_count, count[s[i]])

            while (i-l+1) - max_count > k:
                count[s[l]]-=1
                l+=1
            
            ans = max(ans, i-l+1)
        return ans
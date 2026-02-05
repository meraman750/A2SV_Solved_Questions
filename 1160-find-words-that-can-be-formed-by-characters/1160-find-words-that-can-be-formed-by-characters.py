class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for i in words:
            x = True
            for j in i:
                if i.count(j) > chars.count(j):
                    x = False
                    break
            if x:
                ans += len(i)
        return ans
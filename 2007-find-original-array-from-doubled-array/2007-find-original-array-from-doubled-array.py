class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)

        ans = []
        if len(changed) %2 != 0:
            return []

        for i in sorted(count.keys()):
            while count[i] > 0:
                if count[i*2] < 1:
                    return []
                ans.append(i)
                count[i] -=1
                count[i*2] -=1

        return ans

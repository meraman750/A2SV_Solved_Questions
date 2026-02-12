class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            y = sorted(i)
            x = "".join(y)
            if x in d:
                d[x].append(i)
            else:
                d[x] = [i]
        return list(d.values())
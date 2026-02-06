class Solution:
    def checkEqual(self, a, b) -> bool:
        from collections import Counter
        seta = Counter(a)
        setb = Counter(b)
        
        if len(seta) != len(setb):
            return False
        
        for key, val in seta.items():
            if val != setb[key]:
                return False
        return True

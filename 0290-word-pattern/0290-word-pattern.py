class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        new_s = s.split(" ")
        z = zip(new_s, pattern)
        s = set(z)
        if len(new_s) != len(pattern):
            return False
        a1 = set()
        a2 = set()

        for i in s:
            if i[1] in a1 or i[0] in a2:
                return False
            a1.add(i[1])
            a2.add(i[0])
        return True
        
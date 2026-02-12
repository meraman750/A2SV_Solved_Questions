class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0

        for i in range(len(s1)):
            if s1[i] == "x" and s2[i] == "y":
                xy +=1
            elif s1[i] == "y" and s2[i] == "x":
                yx +=1

        if (xy + yx) % 2 != 0:
            return -1

        one = (xy // 2) + (yx // 2)
        two = 2 * (xy % 2)
        return one + two


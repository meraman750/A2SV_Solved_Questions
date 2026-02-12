class Solution:
    def intToRoman(self, num: int) -> str:
        m = {1: "I",
             4: "IV",
             5: "V",
             9: "IX",
             10: "X",
             40: "XL",
             50: "L",
             90: "XC",
             100: "C",
             500: "D",
             400: "CD",
             900: "CM",
             1000: "M",}

        ans = ""

        for key in sorted(m.keys(), reverse=True):
            if num // key:
                res = num // key
                ans += (m[key] * res)
                num %= key

        return ans

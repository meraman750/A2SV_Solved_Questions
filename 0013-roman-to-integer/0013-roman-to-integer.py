class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4
        }
        ans = 0
        i=0
        while i < len(s):
            if i+1 < len(s) and (s[i] + s[i+1]) in m:
                ans += m[(s[i] + s[i+1])]
                i +=2    
                continue    
            else:
                ans += m[s[i]]
            i+=1
        return ans



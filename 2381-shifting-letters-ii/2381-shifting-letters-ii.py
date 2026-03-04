class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ans = [0] * (len(s)+1)

        for left, right, k in shifts:
            if k == 0:
                ans[left] -=1
                ans[right+1] +=1
            else:
                ans[left] +=1
                ans[right+1] -=1
        
        for i in range(1, len(ans)):
            ans[i] = ans[i] + ans[i-1] 

        temp = []
        for i in range(len(s)):
            temp.append(chr(((((ord(s[i])-97)+ans[i]) % 26) + 97)))

        return "".join(temp)

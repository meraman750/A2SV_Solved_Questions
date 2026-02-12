class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        se = {}

        for dom in cpdomains:
            temp = dom.split(" ")
            count = int(temp[0])
            s = temp[1].split(".")
            cur = ""
            for i in range(len(s)-1, -1, -1):
                if cur:
                    cur = s[i] + "." + cur
                else:
                    cur = s[i]
                if cur in se:
                    se[cur] += count
                else:
                    se[cur] = count
        
        ans = []
        for key, val in se.items():
            temp = str(val) + " " + key
            ans.append(temp)
        return ans

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        adis_response = []

        for i in responses:
            adis_response.append(set(i))

        frequency = defaultdict(int)

        for i in adis_response:
            for j in i:
                frequency[j] +=1
        
        ans = sorted(frequency.keys(), key=lambda x: (-frequency[x], x))
        print(ans)
        return ans[0]
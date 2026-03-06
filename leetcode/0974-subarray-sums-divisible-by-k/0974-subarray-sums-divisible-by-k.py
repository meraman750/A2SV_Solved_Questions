class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sm = 0
        ans = 0
        count = defaultdict(int)
        count[0] +=1

        for i in nums:
            sm += i
            x = sm % k
            ans += count[x]
            count[x]+=1
        return ans  
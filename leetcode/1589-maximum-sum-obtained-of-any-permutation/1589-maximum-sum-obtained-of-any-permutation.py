class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        temp = [0] * (len(nums)+1)

        for l, r in requests:
            temp[l] += 1
            temp[r+1] -= 1

        for i in range(1, len(temp)):
            temp[i] += temp[i-1]
        temp.sort(reverse=True)
        ans = 0
        for key, val in zip(temp, nums):
            if key > 0:
                ans+= (key * val)
        return mod(ans, 10**9 + 7)

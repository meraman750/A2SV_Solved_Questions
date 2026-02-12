class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)
        count = defaultdict(int)
        maxx = 0
        n = len(nums)
        for i in range(n):
            count[nums[i]] +=1

            if count[nums[i]] * 2 > (i+1):
                if (freq[nums[i]] - count[nums[i]]) * 2 > (n-i-1):
                    return i
        return -1
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        count = Counter(nums)
        n = len(nums) / 3

        for key, val in count.items():
            if val > n:
                ans.append(key)
        return ans
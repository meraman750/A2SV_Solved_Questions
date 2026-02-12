class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i in range(len(nums)):
            d[i] = nums[i]
        s = sorted(d.values())
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] + s[right] > target:
                right -=1
            elif s[left] + s[right] < target:
                left +=1
            else:
                left = s[left]
                right = s[right]
                break
        return [key for key, value in d.items() if left == value or right == value]
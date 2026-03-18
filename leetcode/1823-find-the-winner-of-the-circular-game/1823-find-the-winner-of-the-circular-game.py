class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        array = []
        for i in range(1, n+1):
            array.append(i)

        def calc(nums, idx):
            if len(nums) == 1:
                return nums[0]
            idx = (idx+k-1) % len(nums)
            del nums[idx]
            return calc(nums, idx)
             
        return calc(array, 0)

         
            
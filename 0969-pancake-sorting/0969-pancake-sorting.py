class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        adis = sorted(arr) 
        if arr == adis:
            return []

        ans = []
        idx = len(adis)-1
        while idx >= 0:
            x = arr.index(adis[idx])
            if x > 0:
                ans.append(x+1)
            arr[:x+1] = reversed(arr[:x+1])
            if arr == adis:
                break
            if idx > 0:
                ans.append(idx+1)
            arr[:idx+1] = reversed(arr[:idx+1])
            if arr == adis:
                break
            idx -=1

        return ans

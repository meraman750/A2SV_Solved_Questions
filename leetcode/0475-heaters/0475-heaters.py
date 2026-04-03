class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        radius = 0
        heaters.sort()
        for hous in houses:
            left = 0
            right = len(heaters)-1
            min_rad = float("inf")
            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] > hous:
                    right = mid -1
                    min_rad = min(min_rad, abs(hous-heaters[mid]))
                elif heaters[mid] < hous:
                    left = mid + 1
                    min_rad = min(min_rad, abs(hous-heaters[mid]))
                else:
                    min_rad = 0
                    break
            radius = max(radius, min_rad)
        return radius
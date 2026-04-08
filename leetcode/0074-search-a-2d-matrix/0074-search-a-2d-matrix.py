class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        down = len(matrix)-1
        ans = -1
        while top <= down:
            mid = (top+down) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                ans = mid
                break
            elif matrix[mid][0] < target:
                top = mid+1
            else:
                down = mid-1

        if ans == -1:
            return False

        left = 0
        right = len(matrix[ans])-1

        while left <= right:
            one = (left + right) //2
            if matrix[ans][one] == target:
                return True
            elif matrix[ans][one] < target:
                left = one+1
            else:
                right = one-1
        return False
        
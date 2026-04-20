class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) 
        def merge(left, right):
            # print(left, right, ans)
            l=r=0
            temp = []
            while l < len(left) and r < len(right):
                if left[l][0] <= right[r][0]:
                    temp.append(left[l])
                    ans[left[l][1]] += (r)
                    l+=1
                else:
                    temp.append(right[r])
                    r+=1

            while l < len(left):
                temp.append(left[l])
                ans[left[l][1]] += (r)
                l+=1
            while r < len(right):
                temp.append(right[r])
                r+=1
            return temp
                    

        def divide(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left_side = divide(arr[:mid])
            right_side = divide(arr[mid:])

            return merge(left_side, right_side)

        new_nums = [[nums[i], i] for i in range(len(nums))]
        divide(new_nums)
        
        return ans
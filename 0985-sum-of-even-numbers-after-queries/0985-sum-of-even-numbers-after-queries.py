class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = [] * len(nums)

        p_sum = sum(filter(lambda x: x%2==0, nums))
        # print(prev)
        for i in queries:
            if nums[i[1]] % 2 == 0:  
                p_sum -= nums[i[1]]
                
            nums[i[1]] += i[0]

            if nums[i[1]] % 2 == 0:
                p_sum += nums[i[1]] 
            
            ans.append(p_sum)
            
        return ans
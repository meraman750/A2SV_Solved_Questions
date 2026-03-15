class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        costs_one = sorted(costs, key=lambda x: x[0] - x[1])
        ans1 = 0
        count = 0
        for l, r in costs_one:
            if count >= n:
                ans1 += r
            else:
                ans1 += l
            count+=1
        return ans1

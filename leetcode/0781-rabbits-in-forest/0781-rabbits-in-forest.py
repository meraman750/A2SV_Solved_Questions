class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = answers.count(0)
        mp = Counter(answers)
        for key, val in mp.items():
            if key == 0:
                continue

            ans+= (ceil(val / (key+1)) * (key+1))
            # ans +=
        return ans

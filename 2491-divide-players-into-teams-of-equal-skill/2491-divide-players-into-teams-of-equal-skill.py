class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # 1 2 3 3 4 5
        skill.sort()
        prev = -1
        m = len(skill)
        ans = []
        for i in range(m//2):
            average_sum = (skill[i] + skill[m-1-i])
            if prev == -1:
                prev = average_sum
                ans.append(skill[i] * skill[m-1-i])
            else:
                if prev != average_sum:
                    return -1
                else:
                    ans.append(skill[i] * skill[m-1-i])
        return sum(ans)

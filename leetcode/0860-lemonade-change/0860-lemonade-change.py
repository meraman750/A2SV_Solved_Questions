class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mp = defaultdict(int)
        for i in bills:
            if i == 5:
                mp[5] +=1
            elif i == 10:
                if mp[5] == 0:
                    return False
                mp[5]-=1
                mp[10]+=1
            elif i == 20:
                if mp[10] == 0:
                    if mp[5] >= 3:
                        mp[5]-=3
                    else:
                        return False
                        
                elif mp[10] > 0:
                    if mp[5] > 0:
                        mp[5]-=1
                        mp[10]-=1
                    else:
                        return False

                mp[20]+=1
        return True
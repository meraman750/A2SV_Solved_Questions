class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m = {}
        for i in range(len(list1)):
            m[list1[i]] = i
        
        length = float("inf")
        ans = []

        for i in range(len(list2)):
            cur = 0
            if list2[i] in m:
                cur = i + m[list2[i]]
                if cur < length:
                    ans = [list2[i]]
                    length = cur
                elif cur == length:
                    ans.append(list2[i])
        return ans

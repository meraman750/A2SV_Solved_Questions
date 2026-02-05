class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        # l1 = set(list1)
        # l2 = set(list2)
        
        ans = []
        length = float("inf")
        for i in range(len(list1)):
            try:
                idx = list2.index(list1[i])
            except ValueError:
                idx = -1
            if idx != -1:
                if idx + i < length:
                    ans = [list1[i]]
                    length = idx + i
                elif idx + i == length:
                    ans.append(list1[i])

        return list(ans)
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans = 0
        visited = set()
        ma = {e.id: e for e in employees}
        def calc(emp):
            if not emp:
                return 
            nonlocal ans
            visited.add(emp.id) 
            ans += emp.importance

            for node in emp.subordinates:
                if node not in visited:
                    calc(ma[node])

        for i in employees:
            if i.id == id:
                calc(i)
                break
        return ans

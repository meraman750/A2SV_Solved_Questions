class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        arr = [[] for _ in range(n)]

        for i, j in edges:
            arr[i].append(j)
            arr[j].append(i)

        visited = set()
        visited.add(source)
        
        def calc(n):
            if n == destination:
                return True
            
            for i in arr[n]:
                if i not in visited:
                    visited.add(i)
                    if calc(i):
                        return True
            return False
        
        return calc(source) 
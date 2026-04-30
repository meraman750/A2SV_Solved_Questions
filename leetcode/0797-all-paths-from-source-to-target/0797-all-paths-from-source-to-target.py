class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)-1
        ans = []
        def calc(i, temp):
            if i >= len(graph):
                return 
            if i == n:
                ans.append(temp[:])
                return 
            for j in graph[i]:
                temp.append(j)
                calc(j, temp)
                temp.pop()
        
        calc(0, [0])
        return ans
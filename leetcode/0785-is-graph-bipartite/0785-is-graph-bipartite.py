class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        temp = ["a"] * len(graph)
        # a=normal, b=black, g=gray

        def calc(i):
            d = deque()
            d.append(i)
            while d:
                # print(d)
                x = d.popleft()
                visited.add(x)

                for j in graph[x]:
                    if temp[j] == "a":
                        if temp[x] == "b":
                            temp[j] = "g"
                        else:
                            temp[j] = "b"
                        d.append(j)
                    else:
                        if temp[x] == temp[j]:
                            return False
            return True


        visited = set()
        for i in range(len(graph)):
            if i not in visited and temp[i] == "a":
                temp[i] = "b"
                if not calc(i):
                    return False
        return True
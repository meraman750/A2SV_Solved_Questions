class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def calc(i):
            q = deque()
            q.append(bombs[i])
            
            visited = set()
            visited.add(i)

            count = 1
            while q:
                temp = q.popleft()

                for j in range(len(bombs)):
                    x, y, r = bombs[j]
                    if i==j or j in visited:
                        continue

                    distance = sqrt(((x-temp[0])**2) + ((y-temp[1])**2))
                    if distance <= temp[2]:
                        q.append([x, y, r])
                        visited.add(j)
                        count+=1
                        
            return count

        ans = 0
        for i in range(len(bombs)):
            ans = max(ans, calc(i))

        return ans 

                 








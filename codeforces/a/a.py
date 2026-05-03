from collections import deque
def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    l, r = list_()
    arr[l].append(r)
    arr[r].append(l)

# print(arr)
def calc(i):
    visited = [-1] * len(arr)
    d = deque()
    d.append(i)
    visited[i] = 0
    temp = i

    while d:
        x = d.popleft()
      
        for j in arr[x]:
            if visited[j] == -1:
                visited[j] = visited[x] + 1
                d.append(j)
                if visited[j] > visited[temp]:
                    temp = j
    return temp, visited[temp]

cur, tot = calc(1)

cur, tot = calc(cur)

print(tot * 3)
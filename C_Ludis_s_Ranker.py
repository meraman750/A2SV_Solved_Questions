from collections import Counter
n = int(input())

arr = list(map(int, input().split()))

count = {}
for i in range(len(arr)):
    if arr[i] in count:
        count[arr[i]].append(i)
    else:
        count[arr[i]] = [i]

so = sorted(arr, reverse=True)

ans = []
rank = 1
ans.append([so[0], rank])
for i in range(1, len(arr)):
    if so[i] != so[i-1]:
        rank = i+1
        ans.append([so[i], rank])
    else:
        ans.append([so[i], rank])

res = [0] * len(arr)

for i in range(len(arr)):
    x = ans[i][0]
    for j in count[x]:
        res[j] = ans[i][1]

print(" ".join(map(str, res)))



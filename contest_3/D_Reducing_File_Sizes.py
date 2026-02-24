def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, m = list_()
arr = []
for i in range(n):
    b, a = list_()
    arr.append([b, a, b-a])

arr.sort(key=lambda x: -x[2])
cur = sum([arr[i][1] for i in range(len(arr))])
if cur > m:
    print(-1)
    exit(0)

maxx = sum([arr[i][0] for i in range(len(arr))])
i = 0
while maxx > m:
    if i < len(arr):
        maxx = maxx - arr[i][0] + arr[i][1]
        i+=1
    else:
        break
print(i)



def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, k, q = list_()
ns = []
qs = []
minn = float("inf")
maxx = float("-inf")
for _ in range(n):
    l, r = list_()
    ns.append([l, r])
    minn = min(minn, l)
    maxx = max(maxx, r)

for _ in range(q):
    l, r = list_()
    qs.append([l, r])

arr = [0] * 200002

for l, r in ns:
    arr[l] +=1
    arr[r+1] -=1

for i in range(1, len(arr)):
    arr[i] = arr[i] + arr[i-1]

pre = []
count = 0

for i in arr:
    if i >= k:
        count+=1
    pre.append(count)
pre.pop()
pre.append(0)

for l, r in qs:
    ans = 0
    print(pre[r] - pre[l-1])
    

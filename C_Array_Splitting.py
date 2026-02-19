def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

# 4 8 15 16 23 42
# 0 4 7  1  7  19
n, k = list_()
arr = list_()
ans = []
for i in range(1, len(arr)):
    ans.append(arr[i]-arr[i-1])
print(sum(sorted(ans, reverse=True)[k-1:]))


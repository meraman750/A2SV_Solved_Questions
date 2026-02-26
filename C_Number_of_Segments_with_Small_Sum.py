def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, k = list_()

arr = list_()

left = 0
ans = 0
sm = 0
for i in range(n):
    sm+=arr[i]
    while sm > k:
        sm-=arr[left]
        left+=1
    ans += (i-left+1)
print(ans)
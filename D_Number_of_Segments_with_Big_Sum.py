def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, k = list_()
nums = list_()

left = 0
sm = 0
ans = 0
for i in range(n):
    sm += nums[i]
    while sm >= k:
        ans += n-i
        sm-= nums[left]
        left+=1
print(ans)
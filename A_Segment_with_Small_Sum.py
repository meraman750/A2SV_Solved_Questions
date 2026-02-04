def list_(): return list(map(int, input().split()))

n, s = list_()
nums = list_()
sum_ = 0
ans = 0
sl=0
for i in range(n):
    sum_+= nums[i]
    while sum_ > s and sl <= i:
        sum_ -=nums[sl]
        sl+=1
    ans = max(ans, i-sl+1)
print(ans)
n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

l = nums[k-1]

ans = 0
for i in nums:
    if i >= l and l > 0:
        ans+=1

print(ans)
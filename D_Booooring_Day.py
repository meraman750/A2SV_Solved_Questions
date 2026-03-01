def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n, l, r = list_()
    nums = list_()

    left = 0
    cur = 0
    ans = 0

    for i in range(n):
        cur+=nums[i]
        while left <= i and cur > r:
            cur-=nums[left]
            left+=1
        
        if l <= cur <= r:
            ans+=1
            cur = 0
            left = i+1
    
    print(ans)


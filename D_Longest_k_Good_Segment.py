from collections import defaultdict

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, k = list_()
nums = list_()

left = 0
mp = defaultdict(int)
l_ans = 0
r_ans = 0

for i in range(n):
    mp[nums[i]] +=1
    while len(mp) > k and left < n:
        mp[nums[left]]-=1
        if mp[nums[left]] == 0:
            del mp[nums[left]]
        left+=1
    if (i-left+1) > (r_ans - l_ans+1):
        l_ans = left
        r_ans = i

print(l_ans+1, r_ans+1)


from collections import defaultdict

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, k = list_()
nums = list_()

left = 0
s = defaultdict(int)
ans = 0
for i in range(n):
    s[nums[i]] +=1
    while len(s) > k:
        s[nums[left]]-=1
        if s[nums[left]] == 0:
            del s[nums[left]]
        left+=1
    ans+= (i-left+1)
print(ans)

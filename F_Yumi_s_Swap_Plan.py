from collections import Counter, defaultdict

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())
s = input()
count = Counter(s)
s+=s
    
# for T
maxx = count["T"]
temp = defaultdict(int)
left = 0 
ans = float("inf")
for i in range(2*n):
    temp[s[i]] +=1
    if left < n and i-left+1 == maxx:
        ans = min(ans, temp["H"])
        temp[s[left]]-=1
        left+=1

# for H
maxx = count["H"]
temp = defaultdict(int)
left = 0 
for i in range(2*n):
    temp[s[i]] +=1
    if left < n and i-left+1 == maxx:
        ans = min(ans, temp["T"])
        temp[s[left]]-=1
        left+=1

if ans == float("inf"):
    print(0)
else:
    print(ans)
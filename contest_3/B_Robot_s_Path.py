def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, k = list_()
s = input()
count = 1
ans = 0
for i in range(n):
    if s[i] == "#":
        count+=1
    else:
        count=0
    ans = max(ans, count)

if ans >= k:
    print("NO")
else:
    print("YES")


    


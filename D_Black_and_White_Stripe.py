from collections import defaultdict

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n, k = list_()
    s = input()
    count = defaultdict(int)
    ans = float("inf")
    left = 0
    for i in range(n):
        count[s[i]] +=1
        if i-left+1 == k:
            ans = min(ans, count["W"])
            count[s[left]] -=1
            left+=1

    if ans == float("inf"):
        print(0)
    else:
        print(ans)
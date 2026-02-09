from collections import Counter

n = int(input())

for _ in range(n):
    k = int(input())
    s = input()
    
    se = set()
    r = [0] * k
    l = [0] * k
    for i in range(k):
        se.add(s[i])
        r[i] = len(se)

    se = set()
    for i in range(k-1, -1, -1):
        se.add(s[i])
        l[i] = len(se)

    ans = 0
    for i in range(k-1):
        ans = max(ans, r[i] + l[i+1])

    print(ans)

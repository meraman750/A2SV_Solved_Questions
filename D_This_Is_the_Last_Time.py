def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))
# 04

t = int(input())

for _ in range(t):
    n, k = list_()
    mp = []
    for __ in range(n):
        l, r, real= list_()
        mp.append([real, l, r])
    
    adis = sorted(mp)

    for real, l, r in adis:
        if k < l:
            continue
        k = max(k, real)
    print(k)
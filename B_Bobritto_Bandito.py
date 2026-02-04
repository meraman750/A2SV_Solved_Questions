def list_(): return list(map(int, input().split()))

for _ in range(int(input())):
    n,m,l,r = list_()
    if n==m:
        print(l,r)
    else:
        if (l+m) < 0:
            k = 0-(l+m)
            print(l+k, l+m+k)
        else:
            print(l, l+m)
            
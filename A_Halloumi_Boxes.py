def list_(): return list(map(int, input().split()))

t = int(input())

for _ in range(t):

    n, k = list_()
    a = list_()
    
    if k == 1:
        print("YES" if a == sorted(a) else "NO")
    else:
        print("YES")
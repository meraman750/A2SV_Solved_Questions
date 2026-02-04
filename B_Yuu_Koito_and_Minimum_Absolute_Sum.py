def list_(): return list(map(int, input().split()))

t = int(input())

for _ in range(t):
    n = int(input())
    p = list_()

    pos = [0] * (n + 1)
    for i in range(n):
        pos[p[i]] = i

    bad = 0
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            bad += 1

    if bad >= 2:
        print("No")
    else:
        print("Yes")

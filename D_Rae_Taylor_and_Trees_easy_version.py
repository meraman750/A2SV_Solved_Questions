def list_(): return list(map(int, input().split()))

t = int(input())

for _ in range(t):
    n = int(input())
    p = list_()

    pos = [0] * (n + 1)
    for idx, val in enumerate(p):
        pos[val] = idx

    segments = 1
    for i in range(2, n+1):
        if pos[i] < pos[i-1]:
            segments += 1

    print("Yes" if segments == 1 else "No")

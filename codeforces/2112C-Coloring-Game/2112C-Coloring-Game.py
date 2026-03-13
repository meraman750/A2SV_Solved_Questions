def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n = int(input())
    a = list_()
    a.sort()
    ans = 0

    limit = a[-1]

    for k in range(2, n):
        i = 0
        j = k - 1

        while i < j:
            if a[i] + a[j] > a[k] and a[i] + a[j] + a[k] > limit:
                ans += j - i
                j -= 1
            else:
                i += 1

    print(ans)
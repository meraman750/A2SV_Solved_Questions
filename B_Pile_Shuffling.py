def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))


n = int(input())

for _ in range(n):
    k = int(input())

    count = 0
    for _ in range(k):
        a,b,c,d = list_()
        if a > c:
            count += a-c
        if b > d:
            count += (b-d) + min(a,c)
    print(count)

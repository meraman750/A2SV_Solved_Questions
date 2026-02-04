def list_(): return list(map(int, input().split()))

for _ in range(int(input())):
    x, y, a = list_()
    print("NO" if ((a // (x + y)) * (x + y)) + x > a else "YES")
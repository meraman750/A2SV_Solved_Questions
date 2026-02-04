def list_(): return list(map(int, input().split()))

for _ in range(int(input())):
    n, k = list_()
    arr = [0] * (k + 1)
    for a in range(k):
        x, y = list_()
        arr[x] += y
    arr.sort(reverse = True)
    print(sum(arr[:n]))
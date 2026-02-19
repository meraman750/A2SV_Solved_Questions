def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    k = int(input())
    arr = list_()

    adis = sorted(arr)
    x = k//2

    for i in range(1, k):
        if (i+x) < k:
            if arr[i] > arr[i+x]:
                arr[i+x], arr[i] = arr[i], arr[i+x]
    if adis == arr:
        print("YES")
    else:
        print("NO")


    
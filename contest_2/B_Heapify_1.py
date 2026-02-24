def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    k = int(input())
    arr = list_()

    adis = sorted(arr)
    x = k//2

    flag = False
    for __ in range(k):
        for i in range(k):
            if 2*(i+1) <= k:
                if arr[i] > arr[(2*(i+1))-1]:
                    arr[i], arr[(2*(i+1))-1] = arr[(2*(i+1))-1], arr[i]
            if arr == adis:
                flag = True
                break
        if flag:
            break
        
    if adis == arr:
        print("YES")
    else:
        print("NO")
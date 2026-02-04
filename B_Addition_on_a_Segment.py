def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    k=int(input())
    arr=list_()
    sum_b=sum(arr)

    zer = arr.count(0)
    check = k - zer

    for i in range(check, 0, -1):
        if (sum_b - i) >= (k-1):
            print(i)
            break 

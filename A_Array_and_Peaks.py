def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    n, k = list_()

    arr = [x for x in range(1, n+1)]
    if n == k:
        print(-1)
        continue
    if n%2 == 0:
        x = (n//2) -1
        if k > x:
            print(-1)
            continue
        # else: write the code to form the peak array for even numbers
        else:
            l = 1
            while k > 0 and l < len(arr):
                x = arr.pop()
                arr.insert(l, x)
                k-=1
                l+=2
    else:
        x = (n//2)
        if k > x:
            print(-1)
            continue
        # else: write the code to form the peark array for array of ood length
        else:
            l = 1
            while k > 0 and l < len(arr):
                x = arr.pop()
                arr.insert(l, x)
                k-=1
                l+=2
    print(" ".join(map(str, arr)))
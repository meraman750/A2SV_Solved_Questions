def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))
 

n = int(input())

for _ in range(n):
    k = int(input())
    arr = list_()

    if 67 in arr:
        print("YES")
    else:
        print("NO")
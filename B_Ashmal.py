def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    k = int(input())
    arr = str_()
    s = ""
    for i in arr:
        if not s:
            s += i
            continue
        if (i + s) > (s + i):
            s += i
        else:
            s = i + s
         
    print(s)

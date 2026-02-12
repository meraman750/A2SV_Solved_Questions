def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))
# 3:40

n = 5

i = 0
for _ in range(n):
    arr = list_()
    if 1 in arr:
        j = arr.index(1)

        ans = abs(i-2) + abs(j-2)
        print(ans)
        break
    i+=1

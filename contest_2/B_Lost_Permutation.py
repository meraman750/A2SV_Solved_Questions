def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))
 
n = int(input())

for i in range(n):
    m,s = list_()

    arr = list_()
    arr.sort()

    cur = 0
    for i in range(arr[-1]):
        if i not in set(arr):
            cur += i
    i = arr[-1]+1
    while cur + i <= s:
        cur +=i
        i+=1

    if cur != s:
        print("NO")
    else:
        print("YES")

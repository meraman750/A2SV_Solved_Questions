def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))


n = int(input())

for _ in range(n):
    k, l = list_()
    arr = list_()
    arr.sort(reverse=True)
    
    vow = list_()
    vow.sort()

    ans = 0
    f, s = 0, 0
    while s < l:
        if vow[s] == 1:
            f+=1
        else:
            x = vow[s]-1
            ans += sum(arr[f:f+x])
            f += (x+1)
        s+=1    
    ans += sum(arr[f:])
    print(ans)
             


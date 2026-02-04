def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    a,b,c = list_()
    arr = list_() 

    ans = b
    for i in arr:
        # if i < a:
        #     ans+= i 
        # else:
        #     ans += a-1

        ans += min(a-1, i)
            
    print(ans)
def list_(): return list(map(int, input().split()))

n = int(input())

for _ in range(n):
    arr = list_() 
    if len(set(arr)) == 1:
        print("YES")
    else:
        print("NO")



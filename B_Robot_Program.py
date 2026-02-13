def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n, x, k = list_()
    s = input()

    zero = 0

    arr = []
    temp = 0 
    for i in s:
        if i == "L":
            temp -=1
        else:
            temp +=1
        arr.append(temp)

    idx = -1
    for i in range(n):
        if x + arr[i] == 0:
            idx = i+1
            break
    
    if idx == -1 or idx > k:
        print(0)
        continue
    
    zero +=1
    k -= idx
    cycle = -1

    for i in range(n):
        if arr[i] == 0:
            cycle = i+1
            break
    
    if cycle == -1:
        print(zero)
        continue

    zero += k // cycle

    print(zero)

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))
 
n = int(input())
 
for _ in range(n):
    s = input()
    flag = True
    stack = ""
    for i in s:
        if i.islower():
            stack += i
        else:
            if i.lower() not in stack:
                flag = False
                break
    if flag:
        print("YES")
    else:
        print("NO")
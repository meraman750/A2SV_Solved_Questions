def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    k = int(input())
    s = input()
    
    stack = []

    for i in range(k):
        if not stack:
            stack.append(s[i])
            continue
        if s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])

    if stack:
        print("NO")
    else:
        print("YES")
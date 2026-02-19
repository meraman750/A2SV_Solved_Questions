def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    k = int(input())
    s = input()

    prev = {}
    for i in range(k):
        if s[i:i + 2] in prev and i - prev[s[i:i + 2]] > 1:
            print("YES")
            break 
        elif s[i:i + 2] not in prev:
            prev[s[i:i + 2]] = i 
    else:
        print("NO")
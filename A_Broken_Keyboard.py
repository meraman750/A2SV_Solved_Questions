def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    s = input()
    ans = []
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            i+=2
        else:
            ans.append(s[i])
            i+=1
    if i < len(s):
        ans.append(s[i])
    print("".join(sorted(set(ans))))



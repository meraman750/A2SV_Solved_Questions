def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    x = input()
    s = input()

    ans = ""
    flag = True
    for i in range(len(x)):
        idx = s.find(x[i], 0)
        if idx == -1:
            flag = False
            break
        else:
            s = s[:idx] + s[idx+1:]
    if not flag:
        print("Impossible")
        continue
    new_s = sorted(s)
    new_s = "".join(new_s)
    
    l, r = 0,0
    ans = ""
    while l < len(x) and r < len(new_s):
        if x[l] < new_s[r]:
            ans += x[l]
            l+=1
        else:
            ans += new_s[r]
            r+=1
    while l < len(x):
        ans += x[l]
        l+=1
    while r < len(new_s):
        ans += new_s[r]
        r+=1

    print(ans)
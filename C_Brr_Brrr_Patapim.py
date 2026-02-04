def list_(): return list(map(int, input().split()))

for p in range(int(input())):
    t = int(input())
    x = []
    for m in range(t):
        y = list_()
        x.append(y)
    ans = [0] * (2*t)
    for i in range(1, len(ans)):
        if i > t:
            ans[i] = x[i-t][t-1]
        else:
            ans[i] = x[0][i-1]
    l = set(ans)
    for i in range(len(ans)+1):
        if i not in l:
            ans[0] = i
    print(" ".join(map(str, ans)))
    
    
    # for i in x:
    #     for j in i:
    #         if j not in ans:
    #             ans.append(j)
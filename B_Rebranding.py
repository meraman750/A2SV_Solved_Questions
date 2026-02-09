def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, k = list_()
s = input()
ans = {}
for i in range(n):
        if s[i] in ans:
            ans[s[i]].append(i)
        else:
            ans[s[i]] = [i]

for _ in range(k):
    x, y = str_()

    if x in ans and y in ans:
        ans[x], ans[y] = ans[y], ans[x]

    elif x in ans:
        ans[y] = ans.pop(x)

    elif y in ans:
        ans[x] = ans.pop(y)

res = [""] * n
for key, val in ans.items():
     for i in val:
          res[i] = key
    
print("".join(res))


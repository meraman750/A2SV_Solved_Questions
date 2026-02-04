def list_(): return list(map(int, input().split()))

for _  in range(int(input())):
    n,k = list_()
    s = input()
    if n==1:
        print("NO")
        continue

    rev = s[::-1]

    if s < rev:
        print("YES")            
        continue

    if k == 0:
        print("NO")
        continue

    found = False
    s = list(s)

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            s[i], s[j] = s[j], s[i]
            if "".join(s) < "".join(s[::-1]):
                found = True
                break
            s[i], s[j] = s[j], s[i]
        if found:
            break
    if found:
        print("YES")
    else:
        print("NO")
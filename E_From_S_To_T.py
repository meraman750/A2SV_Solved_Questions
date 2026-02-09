from collections import Counter
n = int(input())

for _ in range(n):
    s = input()
    t = input()
    p = input()

    count_p = Counter(p)
    count_t = Counter(t)
    count_s = Counter(s)

    i = 0
    for ch in t:
        if i < len(s) and s[i] == ch:
            i+=1
            
    if i < len(s):
        print("NO")
        continue

    ok = True
    for i in count_t:
        need = count_t[i] - count_s[i]
        if need > count_p[i]:
            print("NO")
            break
            
    else:
        print("YES")


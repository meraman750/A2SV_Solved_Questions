n = int(input())

for _ in range(n):
    k = int(input())
    s = input()
    if "2026" in s or "2025" not in s:
        print(0)
        continue
    if "2025" in s:
        print(1)
        continue
    x = "2026"
    temp = ""
    op = 4
    for i in x:
        temp += i
        if temp in s:
            op-=1
    print(op)



def list_(): return list(map(int, input().split()))

for _ in range(int(input())):
    s = list(map(str, input().split()))
    c = []
    for i in s:
        c.append(i[0])
    print("".join(c))
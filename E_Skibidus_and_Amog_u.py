def list_(): return list(map(int, input().split()))

for _ in range(int(input())):
    x = input()
    if x.endswith("us"):
        x = x[:-2]
        y = list(x)
        y.append('i')
        print(''.join(map(str, y)))

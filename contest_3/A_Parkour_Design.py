def list_(): 
    return list(map(int, input().split()))

t = int(input())

for _ in range(t):
    x, y = list_()

    if (x - 2*y) % 3 != 0:
        print("NO")
        continue

    if y >= 0:
        if x >= 2*y:
            print("YES")
        else:
            print("NO")
    else:
        if x >= -4*y:
            print("YES")
        else:
            print("NO")
def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, q, m = list_()

arr = list_()

qs = [list_() for _ in range(q)]

im = list_()

for i in range(m):
    idx = im[i]
    for j in range(q-1, -1, -1):
        x,y,z = qs[j]
        # print(idx)
        if y <= idx <= z:
            if x == 1:
                idx -= 1
                if idx < y:
                    idx = z
            else:
                idx = (y + z) - idx
        # print(idx)
        # break
    # print("-----")
    # break
    print(arr[idx-1], end=" ")


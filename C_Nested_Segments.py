def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())
arr = []
count = 1
for _ in range(t):
    x, y = list_()
    arr.append([x, y, count])
    count+=1
arr.sort(key=lambda x: (x[0], -x[1]))

j = 0
for x in range(1, len(arr)):
    if arr[x][1] <= arr[j][1]:
        print(arr[x][2], arr[j][2])
        break
    else:
        j = x
else:
    print(-1, -1) 

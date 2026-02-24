def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))
 
n = int(input())
arr = []
count = 1
for _ in range(n):
    x, y = list_()
    arr.append([x, y, count])
    count+=1

arr.sort(key=lambda x: (x[0], -x[1]))

j = 0
for x in range(1, len(arr)):
    if arr[x][1] <= arr[j][1]:
        print(arr[x][2])
        break
    elif (x+1 < len(arr) and arr[j][1] >= arr[x][0] and arr[x+1][0] <= arr[x][1]) and arr[j][1]+1 >= arr[x+1][0] and arr[x][1] <= arr[x+1][1]:
        print(arr[x][2])
        break
    else:
        j = x
else:
    print(-1) 

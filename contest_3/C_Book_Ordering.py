def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())
arr = []
for _ in range(n):
    temp = list_()
    temp.sort()
    arr.append(temp)

maxx = arr[0][1]
for i in range(1, len(arr)):
    if maxx < arr[i][0]:
        print("NO")
        break
    else:
        if maxx >= arr[i][1]:
            maxx = arr[i][1]
        else:
            maxx = arr[i][0]
else:
    print("YES")

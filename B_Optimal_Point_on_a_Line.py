def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())
arr = list_()

arr.sort()
if len(arr) % 2 == 0:
    idx = (len(arr) // 2) -1
else:
    idx = len(arr) // 2
print(arr[idx])
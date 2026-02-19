def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())
arr = list_()
arr.sort()
idx = 0
ans = 0
count = 1
while idx < len(arr):
	if arr[idx] >= count:
		ans+=1
		count+=1
	idx+=1
print(ans)



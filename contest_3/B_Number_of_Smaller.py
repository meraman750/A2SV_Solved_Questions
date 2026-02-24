def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, k = list_()

arr = list_()
nums = list_()
ans = []
count = 0

for i in nums:
    while count < len(arr) and arr[count] < i:
        count +=1
    ans.append(count)

print(*ans)

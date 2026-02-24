def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())
arr = list_()
arr.sort()
nums = [num for num in range(1, n+1)]
for i in range(len(arr)):
    if nums[i] != arr[i]:
        print(nums[i])
        break
else:
    print(n)

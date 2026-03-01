def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, k = list_()
nums = list_()
# arr = {}
# for i in range(n):
#     arr[nums[i]] = i+1
arr = [[nums[x], x+1] for x in range(len(nums))]

# new_arr = sorted(arr.keys(), key=lambda x: x)
arr.sort()
sm = 0
ans = []
i = 0
while i < len(arr) and sm + arr[i][0] <= k:
    sm += arr[i][0]
    ans.append(arr[i][1])
    i+=1

print(len(ans))
print(*(ans))

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    t = int(input())
    nums = list_()

    nums.sort(reverse=True)
    ans = 0
    for i in range(1, len(nums), 2):
        ans += nums[i]
    print(ans)
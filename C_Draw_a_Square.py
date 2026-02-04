def list_(): return list(map(int, input().split()))

for _ in range(int(input())):
    nums = list_()
    n = set(nums)
    if len(n) > 1:
        print("No")
    else:
        print("Yes")
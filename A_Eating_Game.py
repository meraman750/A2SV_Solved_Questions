from collections import Counter

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    k = int(input())
    nums = list_()

    count = Counter(nums)

    maxx = max(nums)
    print(count[maxx])

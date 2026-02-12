from collections import defaultdict

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):

    n, k = list_()
    nums = list_()
    
    d = defaultdict(int)

    for num in nums:
        idx = 0
        if num % k == 0:
            idx = 0
        else:
            idx = k - (num % k)
        d[idx] +=1

    maxx = 0
    for key, val in d.items():
        if key == 0:
            continue
        temp = (val-1) * k + (key)
        maxx = max(maxx, temp+1)

    print(maxx)
    

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n, l, r = list_()
    nums = list_()

    inner = nums[l:r]
    outer = nums[:l] + nums[r:]
    arr = []
    
    if inner:
        minn = min(inner)
        idx = inner.index(minn)
        arr = inner[idx:]
        idx-=1
        while idx >= 0:
            arr.append(inner[idx])
            idx-=1

    if outer:
        for i in range(len(outer)):
            if outer[i] > arr[0]:
                print(*(outer[:i] + arr + outer[i:]))
                break
    else:
        print(*arr)
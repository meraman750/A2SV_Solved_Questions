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
        i = 0
        while i < idx:
            arr.append(inner[i])
            i+=1

    for i in range(len(outer)):
        # if outer(i) < 
        if outer[i] >= arr[0]:
            print(*(outer[:i] + arr + outer[i:]))
            break
    
    else:
        print(*(outer + arr))

#[[0, 0, 0, 0, 0, 0,     0], 
# [0, 3, 3, 4, 8, 10,    0], 
# [0, 8, 14, 18, 24, 27, 0], 
# [0, 9, 17, 21, 28, 36, 0], 
# [0, 13, 22, 26, 34, 49,0], 
# [0, 14, 23, 30, 38, 58,0], 
# [0, 0, 0, 0, 0, 0,     0]]
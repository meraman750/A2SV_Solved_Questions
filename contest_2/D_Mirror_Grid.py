def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

def rotator(nums):
    temp  = []
    for j in range(len(nums)):
        cur = []
        for i in range(len(nums)-1, -1, -1):
            cur.append(nums[i][j])
        temp.append(cur)
    return temp

for _ in range(n):
    k = int(input())
    arr1 = []
    for i in range(k):
        arr1.append(list(map(int, input())))
    
    arr2 = rotator(arr1)
    arr3 = rotator(arr2)
    arr4 = rotator(arr3)

    ans = 0
    for i in range(k):
        for j in range(k):
            zero = [arr1[i][j], arr2[i][j], arr3[i][j], arr4[i][j]].count(0)
            ans += min(zero, 4-zero)
    print(ans // 4)
from collections import Counter

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, k = list_()

arr1 = list_()
arr2 = list_()

count1 = Counter(arr1)
count2 = Counter(arr2)

ans = 0
s1 = set(arr1)
s2 = set(arr2)

for i in s1:
    if i in s2:
        ans += (count1[i] * count2[i])

print(ans)



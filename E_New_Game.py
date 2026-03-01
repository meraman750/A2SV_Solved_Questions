from collections import Counter

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    cards, k = list_()
    nums = list_()

    nums.sort()
    count = Counter(nums)
    key = [i for i in sorted(count.keys())]
    
    left = 0
    temp = count[key[left]]
    ans = temp

    for i in range(1, len(key)):
        if key[i] == key[i-1]+1:
            temp +=count[key[i]]
        else:
            left = i
            temp = count[key[i]]

        while i-left+1 > k:
            temp -= count[key[left]]
            left+=1
        ans = max(ans, temp)
     
    print(ans)

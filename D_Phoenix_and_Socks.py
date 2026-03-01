from collections import Counter

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))
 
t = int(input())

for _ in range(t):
    tot, l, r = list_()
    arr = list_()
    left = arr[:l]
    right = arr[l:]
    left.sort()
    right.sort()
    
    count_left = Counter(left)
    count_right = Counter(right)
    ans = 0
    print(count_right)
    print(count_left)

    if l == r:
        for key, val in count_right.items():
            if key not in count_left:
                ans+=1

        print(ans)
        continue
    # else:
    #     if len(left) > len(right):
    #         for key, val in count_left.items():
    #             if key not in count_right:
    #                 ans+= 


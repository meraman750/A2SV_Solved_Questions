from collections import Counter

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))
 
t = int(input())

for _ in range(t):
    tot, l, r = list_()
    arr = list_()
    left = arr[:l]
    right = arr[l:]
    
    count_left = Counter(left)
    count_right = Counter(right)
    
    for key, val in count_left.items():
        x = min(val, count_right[key])
        count_left[key]-= x
        count_right[key]-= x
        l-=x
        r-=x

    if l == r:
        print(l)
        continue

    if l > r:
        count_left, count_right = count_right, count_left
        l, r = r, l
        
    need = (r-l)//2
    ans = 0
    for key, val in count_right.items():
        while val > 1 and need > 0:
            # print(key, val, need)
            count_right[key]-=2
            val-=2
            need-=1
            ans+=1

    ans += (need * 2)
    ans += l

    print(ans)



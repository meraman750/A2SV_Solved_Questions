from collections import Counter

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    k = int(input())
    one = input()
    two = input()
    def flip(x): return "0" if x =="1" else "1"
    mp = Counter(one)
    flag = False
    for i in range(k-1, -1, -1):
        if flag:
            temp = flip(one[i])
        else:
            temp = one[i]

        if temp != two[i]:
            if mp["0"] != mp["1"]:
                print("NO")
                break
            if flag:
                flag = False
            else:
                flag = True
        # if flag:
        #     x = flip(one[i])
        mp[one[i]]-=1 
    else:
        print("YES")
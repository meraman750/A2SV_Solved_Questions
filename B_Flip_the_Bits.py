from collections import defaultdict

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    k = int(input())
    one = input()
    two = input()
    
    mp = defaultdict(int)
    flag = True

    for i in range(k):
        if one[i] != two[i]:
            mp[one[i]] +=1
        else:
            if mp["0"] != mp["1"]:
                flag = False
                break
            else:
                mp["0"] = 0
                mp["1"] = 0

    if mp["0"] != mp["1"]:
        flag=False
    
    print("YES" if flag else "NO")
from collections import Counter

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    k = int(input())
    a, b = str_()
    
    flag = True
    for i in a:
        if a.count(i) != b.count(i):
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")



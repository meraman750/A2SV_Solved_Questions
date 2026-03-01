from collections import Counter

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    s = input()
    counter = Counter(s)
    count = 0
    
    for key, val in counter.items():
        if val >= 2:
            count+=1
    if count >= 2:
        print("YES")
    else:
        print("NO")
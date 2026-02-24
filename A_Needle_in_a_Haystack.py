from collections import Counter

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    x = input()
    s = input()

    countx = Counter(x)
    counts = Counter(s)
    flag = False
    for key, val in countx.items():
        if counts[key] < val:
            flag = True
            break
        counts[key] -= val
        if counts[key] == 0:
            del counts[key]

    if flag:
        print("Impossible")
        continue
    
    new_s = sorted(counts.keys())
    ans = []
    
    j = 0
    i = 0
    while i < len(new_s) and j < len(x):
        if new_s[i] < x[j]:
            ans.append(new_s[i] * counts[new_s[i]])
            i+=1
        else:
            ans.append(x[j])
            j+=1
    while i < len(new_s):
        ans.append(new_s[i] * counts[new_s[i]])
        i+=1
        
    ans.extend(x[j:])
    print("".join(ans))
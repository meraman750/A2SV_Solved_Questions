def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    k = int(input())
    arr = list_()
    count = 0
    s = set()
    for i in arr:
        if i-1 not in s:
            count+=1    
            s = set()
        s.add(i)
    print(count)

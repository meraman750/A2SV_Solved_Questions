def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))
# 15

t = int(input())

for _ in range(t):
    n = int(input())
    a = list_()
    b = list_()

    count = 0
    ans = []
    
    while True:
        flag = True
        for i in range(n):
            if i+1 < n and a[i] > a[i+1]:
                flag = False
                a[i], a[i+1] = a[i+1], a[i]
                count+=1
                ans.append([1, i+1])
            
            if a[i] > b[i]:
                flag = False
                a[i], b[i] = b[i], a[i]
                count+=1
                ans.append([3, i+1])
            
            if i+1 < n and b[i] > b[i+1]:
                flag = False
                b[i], b[i+1] = b[i+1], b[i]
                count+=1
                ans.append([2, i+1])
        if flag:
            break
    print(count)
    for i, j in ans:
        print(i, j)
            
    
def check(count, ans, a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            ans.append([3, i+1])
            a[i], b[i] = b[i], a[i]
            count+=1
    
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count+=1
                ans.append([1, j+1])

        for j in range(len(a)-i-1):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                count+=1
                ans.append([2, j+1])

    return count, ans, a, b
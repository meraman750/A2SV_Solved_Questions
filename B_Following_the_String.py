import string

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())


for _ in range(n):
    
    s = {}
    for i in string.ascii_lowercase:
        s[i] = 0

    k = int(input())
    arr = list_()
    j = 0 

    ans = ""
    for i in range(k):
        for key, value in s.items():
            if value == arr[i]:
                ans += key
                s[key] += 1
                break
    print(ans)


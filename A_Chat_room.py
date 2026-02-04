def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

s = input()
st = "hello"

i = 0
j = 0
while j < len(st):
    while i < len(s):
        if s[i] == st[j]:
            i += 1
            j+=1
            break
        i += 1
    else:
        if i == len(s):
            break

if j == len(st):
    print("YES")
else:
    print("NO")


def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

c = 0
s = 0
arr = []
adis = []
for _ in range(n):
    temp = list_()
    temp = temp[1:]
    adis.extend(temp)
    arr.append(temp)

adis.sort()
mp = {}
for i in range(len(adis)-1):
    mp[adis[i]] = adis[i+1]

for i in arr:
    for j in range(len(i)-1):
        if i[j] in mp and i[j+1] != mp[i[j]]:
            s+=1
        elif i[j] not in mp:
            s+=1

print(s, s+n-1)

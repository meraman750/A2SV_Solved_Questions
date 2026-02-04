def list_(): return list(map(int, input().split()))

for _ in range(int(input())):
    l = [0,1,0,3,2,0,2,5]
    x = int(input())
    nums = list_()
    count = 0
    z=0
    for i in nums:
        if i in l:
            l.remove(i)
        count+=1
        if len(l) == 0:
            print(count)
            z=1
            break
    if z == 0:
        print("0")    



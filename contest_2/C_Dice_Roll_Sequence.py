def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    k = int(input())
    arr = list_()

    count = 0
    for i in range(k):
        if i-1 >= 0 and (7 - arr[i-1] == arr[i] or arr[i-1] == arr[i]):
            count +=1
    print(count)
            
            


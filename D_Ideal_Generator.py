def list_(): return list(map(int, input().split()))

for _ in range(int(input())):
    x = int(input())
    if x%2==0:
        print("NO")
    else:
        print("Yes")
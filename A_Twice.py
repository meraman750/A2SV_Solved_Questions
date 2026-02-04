def list_(): return list(map(int, input().split()))

for _ in range(int(input())):
    x = int (input())
    nums = list_()
    n = [0] * (x+1)
    for i in nums:
        n[i] += 1
    count = 0
    for i in n:
        count+= i//2
    print(count)
    
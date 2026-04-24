def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n = int(input())
    # print(n)
    ans = [[[], []] for i in range(n+1)]

    for i in range(n):
        temp = input()
        # print(temp)
        for j in range(len(temp)):
            if temp[j] == "1":
                if j > i:
                    ans[i+1][1].append(j+1)
                elif j < i:
                    ans[i+1][0].append(j+1)
            else:
                if j > i:
                    ans[i+1][0].append(j+1)
                elif j < i:
                    ans[i+1][1].append(j+1)
    # print(ans)
    res = [0] * n
    for i in range(len(ans)):
        # print(ans[i][0], ans[i][1])
        res[len(ans[i][0])] = i
    print(*res)
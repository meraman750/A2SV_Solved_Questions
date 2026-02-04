def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))
def brac(): return list(input().split())


n = int(input())

for _ in range(n):
    k = int(input())
    b = str_()
    b = b[0]

    stack = []
    ans = ""
    for i in b:
        if i == "(":
            stack.add(i)
        else:
            stack.pop()
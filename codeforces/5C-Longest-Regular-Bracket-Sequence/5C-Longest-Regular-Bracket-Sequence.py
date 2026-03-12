from collections import defaultdict

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

s = input()
stack = []
ans = 0
maxx = 0
count = 0
flag = True
# print(len(s))

stack = []
nums = []
ans = 0
for i in s:
    if i == "(":
        stack.append(i)
    elif i == ")":
        x = 0 
        while stack and isinstance(stack[-1], int):
            x += stack.pop()
        
        if stack and stack[-1] == "(":
            stack.pop()
            while stack and isinstance(stack[-1], int):
                x += stack.pop()
            stack.append(x+2)
        else:
            stack.append(x)
            stack.append(i)

    # print(stack)
maxx = 0
for i in stack:
    if isinstance(i, int):
        maxx = max(maxx, i)
if maxx == 0:
    print(0, 1)
else:
    print(maxx, stack.count(maxx))
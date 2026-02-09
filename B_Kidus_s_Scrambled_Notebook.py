n = int(input())

for _ in range(n):
    s = input()
    num = int(s)
    k = len(s)
    a = int(s[0])
    flag = False
    for i in range(1, len(s)):
        if s[i] != "0":
            new_a = a * (10**(k-i))
            b = num - new_a
            if b > a:
                flag = True
                print(a, b)
                break
        a *= 10
        a += int(s[i])
    if not flag:
        print(-1)

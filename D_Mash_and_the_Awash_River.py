n = int(input())

for _ in range(n):
    s = input()
    if "**" in s or "*<" in s or ">*" in s or "><" in s:
        print(-1)
        continue
    
    print(len(s) - min(s.count(">"), s.count("<")))

    

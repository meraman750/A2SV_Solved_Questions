from collections import Counter

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for _ in range(n):
    k = int(input())
    s = input()
    
    ans = float("inf")
    for i in range(k):
        count_a = 0
        count_b = 0
        count_c = 0
        for j in range(i, min(i+7, k)):
            if s[j] == "a":
                count_a +=1
            elif s[j] == "b":
                count_b +=1
            elif s[j] == "c":
                count_c +=1
            length = j-i+1

            if length >=2 and count_a > count_b and count_a > count_c:
                ans = min(ans, length)
    if ans == float("inf"):
        print(-1)
        continue
    print(ans)

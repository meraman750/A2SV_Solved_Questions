def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n, m = list_()
    a = list_()
    b = list_()

    b.sort()

    prev = float("-inf")

    for i in a:

        left = 0
        right = m-1

        while left <= right:

            mid = (left + right) // 2
            
            if b[mid] - i >= prev:
                right = mid - 1
            else:
                left = mid + 1
        
        best = float("inf")

        if i >= prev:
            best = i

        if left < m:
            cur = b[left]-i
            if cur >= prev:
                best = min(best, cur)

        if best == float("inf"):
            print("NO")
            break
        prev = best
    else:
        print("YES")
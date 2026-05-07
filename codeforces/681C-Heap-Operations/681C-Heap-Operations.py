import heapq
def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())
s = []
for _ in range(t):
    temp = str_()
    s.append(temp)

nums = []
ans = []

for op in s:
    if op[0] == 'insert':
        x = int(op[1])
        heapq.heappush(nums, x)
        ans.append(['insert', x])
        
    elif op[0] == 'removeMin':
        if not nums:
            heapq.heappush(nums, 0)
            ans.append(['insert', 0])

        heapq.heappop(nums)
        ans.append(['removeMin'])

    else:
        x = int(op[1])
        while nums and nums[0] < x:
            heapq.heappop(nums)
            ans.append(['removeMin'])

        if not nums or nums[0] > x:
            heapq.heappush(nums, x)
            ans.append(['insert', x])

        ans.append(['getMin', x])

print(len(ans))
for op in ans:
    if op[0] == 'removeMin':
        print('removeMin')
    else:
        print(op[0], op[1])
def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list_()

    j = 1
    prev = nums[0]
    ans = [prev]
    
    while j < len(nums)-1:
        if nums[j] > prev:
            if nums[j+1] < nums[j]:
                ans.append(nums[j])
        else:
            if nums[j+1] > nums[j]:
                ans.append(nums[j])

        prev = nums[j]
        j+=1

    ans.append(nums[-1])

    print(len(ans))
    print(*ans)
            

        
        
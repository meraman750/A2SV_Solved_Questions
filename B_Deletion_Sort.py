def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    k = int(input())
    nums = list_()
    prev = nums 

    while len(nums) > 0:
        i = 0
        while i < len(nums):
            temp = nums
            temp.remove(temp[i])
            if  temp != sorted(temp):
                nums.remove(nums[i])
                break

        # print(nums)
        if nums == prev:
            print(len(nums))
            break
        else:
            prev = nums
        
    
                

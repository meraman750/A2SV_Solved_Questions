def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

def var2(arr, nums):
    one, two = 0, 0
    adis = []
    while one < len(arr) or two < len(nums):
        if one < len(arr) and two < len(nums):
            if nums[two] < arr[one]:
                adis.append(nums[two])
                two+=1
            else:
                adis.append(arr[one])
                one+=1
        elif one < len(arr):
            adis.append(arr[one])
            one+=1
        elif two < len(nums):
            adis.append(nums[two])
            two+=1

    return adis


n, m = list_()
arr = list_()
nums = list_()

print(*(var2(arr, nums)))


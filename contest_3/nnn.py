def var2(arr, target):
    left = 0
    right = len(arr) -1
    while left < right:
        if arr[left] + arr[right] > target:
            right-=1
        elif arr[left] + arr[right] < target:
            left +=1
        else:
            return arr[left], arr[right]
        
arr = [2,3,4,5,6,7,8]
print(var2(arr, 7))
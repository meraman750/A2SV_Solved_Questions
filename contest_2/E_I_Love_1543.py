def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for  _  in range(n):
    row, col = list_()

    arr = []
    for i in range(row):
        temp = []
        num = input()
        for j in num:
            temp.append(int(j))
        arr.append(temp)
    
    first = 0
    last = row -1
    left = 0
    right = col-1
    s = "1543"
    ans = 0
    while first < last and left < right:
        temp = ""

        for i in range(left, right+1):
            temp += str(arr[first][i])

        for i in range(first+1, last):
            temp += str(arr[i][right])

        if first < last:
            for i in range(right, left-1, -1):
                temp += str(arr[last][i])
        if left < right:
            for i in range(last-1, first, -1):
                temp += str(arr[i][left])
        
        first +=1
        last -=1
        left +=1
        right -=1
        
        string = temp + temp
        for i in range(len(temp)):
            if string[i:i+4] == s:
                ans +=1
    print(ans)
        

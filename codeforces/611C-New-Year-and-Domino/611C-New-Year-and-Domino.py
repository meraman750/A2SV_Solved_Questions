def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

row, col = list_()
matrix = []
for _ in range(row):
    temp = list(map(str, input()))
    matrix.append(temp)
q = int(input())
qs = []
for _ in range(q):
    temp = list_()
    qs.append(temp)

vertical_matrix = [[0] * (len(matrix[0])+1) for _ in range((len(matrix))+1)]
horizontal_matrix = [[0] * (len(matrix[0])+1) for _ in range((len(matrix))+1)]

count = 0
prev = matrix[0][0]
for j in range(1, col):
    if prev == ".":
        if matrix[0][j] == ".":
            count+=1

    horizontal_matrix[0][j] = count
    prev = matrix[0][j]

count = 0
prev = matrix[0][0]
for i in range(1, row):
    if prev == ".":
        if matrix[i][0] == ".":
            count+=1

    vertical_matrix[i][0] = count
    prev = matrix[i][0]

for i in range(1, row):
    for j in range(1, col):
        x = vertical_matrix[i][j-1] + vertical_matrix[i-1][j] - vertical_matrix[i-1][j-1]
    
        if matrix[i][j] == ".":
            if matrix[i-1][j] == ".":
                x+=1

        vertical_matrix[i][j] = x

for i in range(1, row):
    for j in range(1, col):
        x = horizontal_matrix[i][j-1] + horizontal_matrix[i-1][j] - horizontal_matrix[i-1][j-1]
    
        if matrix[i][j] == ".":
            if matrix[i][j-1] == ".":
                x+=1

        horizontal_matrix[i][j] = x



for r1, c1, r2, c2 in qs:
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    ver = vertical_matrix[r2][c2] - vertical_matrix[r1][c2] - vertical_matrix[r2][c1-1] + vertical_matrix[r1][c1-1]
    hor = horizontal_matrix[r2][c2] - horizontal_matrix[r1-1][c2] - horizontal_matrix[r2][c1] + horizontal_matrix[r1-1][c1]
    print(ver+hor)
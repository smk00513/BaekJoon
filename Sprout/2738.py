row, col = map(int, input().split())
mat1 = []
mat2 = []
for i in range(row):
    mat1.append(list(map(int, input().split())))
for i in range(row):
    mat2.append(list(map(int, input().split())))
for i in range(row):
    result = []
    for j in range(col):
        result.append(mat1[i][j] + mat2[i][j])
    print(*result)
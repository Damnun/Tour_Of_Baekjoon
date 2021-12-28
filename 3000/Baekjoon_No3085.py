def check(matrix, start_row, end_row, start_col, end_col):
    n = len(matrix)
    ans = 1
    for i in range(start_row, end_row + 1):
        cnt = 1
        for j in range(1, n):
            if matrix[i][j] == matrix[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    for i in range(start_col, end_col + 1):
        cnt = 1
        for j in range(1, n):
            if matrix[j][i] == matrix[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    return ans


n = int(input())
matrix = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if j + 1 < n:
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
            temp = check(matrix, i, i, j, j + 1)
            if ans < temp:
                ans = temp
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
        if i + 1 < n:
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
            temp = check(matrix, i, i + 1, j, j)
            if ans < temp:
                ans = temp
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
print(ans)


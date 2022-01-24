n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
check = [[False] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, px, py, color):
    if check[x][y]:
        return True
    check[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if (nx, ny) == (px, py):
                continue
            if a[nx][ny] == color:
                if dfs(nx, ny, x, y, color):
                    return True
    return False


for i in range(n):
    for j in range(m):
        if check[i][j]:
            continue
        if dfs(i, j, -1, -1, a[i][j]):
            print("Yes")
            exit()
print("No")

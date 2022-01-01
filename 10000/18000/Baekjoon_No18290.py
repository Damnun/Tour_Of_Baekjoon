import sys
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def go(prev_x, prev_y, cnt, s):
    if cnt == k:
        global ans
        if ans < s:
            ans = s
        return

    for x in range(prev_x, n):
        for y in range((prev_y if x == prev_x else 0), m):
            if check[x][y]:
                continue
            ok = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if check[nx][ny]:
                        ok = False
            if ok:
                check[x][y] = True
                go(x, y, cnt + 1, s + matrix[x][y])
                check[x][y] = False

ans = -2147483647
n, m, k = map(int, input().split())
check = [[False] * m for _ in range(n)]
matrix = [list(map(int, input().split())) for _ in range(n)]
go(0, 0, 0, 0)
print(ans)

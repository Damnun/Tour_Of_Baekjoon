import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    global o, v
    queue = deque()
    queue.append((a, b))

    to, tv = 0, 0
    if matrix[a][b] == 'o':
        to += 1
    elif matrix[a][b] == 'v':
        tv += 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0 and matrix[nx][ny] != '#':
                if matrix[nx][ny] == 'o':
                    to += 1
                elif matrix[nx][ny] == 'v':
                    tv += 1
                visited[nx][ny] = 1
                queue.append((nx, ny))
    if to and tv:
        if to > tv: v -= tv
        else: o -= to


r, c = map(int, input().split())
matrix = []
visited = [[0] * c for _ in range(r)]
o, v = 0, 0

for i in range(r):
    z = list(input().strip())
    for j in range(c):
        if z[j] == 'o': o += 1
        if z[j] == 'v': v += 1
    matrix.append(z)

for i in range(r):
    for j in range(c):
        if (matrix[i][j] == 'o' or matrix[i][j] == 'v') and visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i, j)
print(o, v)


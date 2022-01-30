from collections import deque
from sys import stdin
input = stdin.readline

n, m, k = map(int, input().split())
a = [input() for _ in range(n)]
queue = deque([(0, 0, 0, 1, 0)])
visited =[[[float('inf')] * (k + 1) for __ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited[0][0][0] = 1

while queue:
    x, y, z, t, d = queue.popleft()
    if visited[x][y][z] != t:
        continue
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == '0' and visited[nx][ny][z] > t + 1:
                visited[nx][ny][z] = t + 1
                queue.append((nx, ny, z, t + 1, (d + 1) % 2))

            if z < k and a[nx][ny] == '1':
                if d == 0 and visited[nx][ny][z + 1] > t + 1:
                    visited[nx][ny][z + 1] = t + 1
                    queue.append((nx, ny, z + 1, t + 1, (d + 1) % 2))

                if d == 1 and visited[nx][ny][z + 1] > t + 2:
                    visited[nx][ny][z + 1] = t + 2
                    queue.append((nx, ny, z + 1, t + 2, d))
ans = min(visited[n - 1][m - 1])
print([ans, -1][ans == float('inf')])

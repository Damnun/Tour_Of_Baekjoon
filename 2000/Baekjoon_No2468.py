from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(px, py, h):
    queue = deque()
    queue.append((px, py))
    visited[px][py] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and a[nx][ny] > h:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

ans = 1
for k in range(max(map(max, a))):
    visited = [[False] * n for _ in range(n)]
    safe = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] > k and not visited[i][j]:
                safe += 1
                bfs(i, j, k)
    ans = max(ans, safe)
print(ans)

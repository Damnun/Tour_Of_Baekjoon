from collections import deque
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
dist = [[[0] * 2 for j in range(m)] for i in range(n)]
dist[0][0][0] = 1

queue = deque()
queue.append((0, 0, 0))
while queue:
    x, y, break_count = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 1 and break_count == 0 and dist[nx][ny][break_count + 1] == 0:
                dist[nx][ny][break_count + 1] = dist[x][y][break_count] + 1
                queue.append((nx, ny, break_count + 1))
            if a[nx][ny] == 0 and dist[nx][ny][break_count] == 0:
                dist[nx][ny][break_count] = dist[x][y][break_count] + 1
                queue.append((nx, ny, break_count))


if dist[n - 1][m - 1][0] and dist[n - 1][m - 1][1]:
    print(min(dist[n - 1][m - 1]))
elif dist[n - 1][m -1][0]:
    print(dist[n - 1][m - 1][0])
elif dist[n - 1][m - 1][1]:
    print(dist[n - 1][m - 1][1])
else:
    print(-1)

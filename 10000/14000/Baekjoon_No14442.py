from collections import deque
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

n, m, k = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
dist = [[[0] * 11 for j in range(m)] for i in range(n)]
dist[0][0][0] = 1

queue = deque()
queue.append((0, 0, 0))
while queue:
    x, y, break_count = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 1 and break_count + 1 <= k and dist[nx][ny][break_count + 1] == 0:
                dist[nx][ny][break_count + 1] = dist[x][y][break_count] + 1
                queue.append((nx, ny, break_count + 1))
            if a[nx][ny] == 0 and dist[nx][ny][break_count] == 0:
                dist[nx][ny][break_count] = dist[x][y][break_count] + 1
                queue.append((nx, ny, break_count))


ans = -1
for i in range(k + 1):
    if dist[n - 1][m - 1][i] == 0:
        continue
    if ans == -1:
        ans = dist[n - 1][m - 1][i]
    elif ans > dist[n - 1][m - 1][i]:
        ans = dist[n - 1][m - 1][i]
print(ans)

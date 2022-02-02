from collections import deque
n, m = map(int, input().split())
a = [input() for _ in range(m)]
d = [[-1] * n for _ in range(m)]
sx = sy = ex = ey = -1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(m):
    for j in range(n):
        if a[i][j] == 'C':
            if sx == -1:
                sx, sy = i, j
            else:
                ex, ey = i, j

d[sx][sy] = 0
queue = deque()
queue.append((sx, sy))
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 한 점을 기준으로 갈 수 있는 상하좌우 모두를 입력시켜줌
        # 그 점에서 나아가서 또 상하좌우를 이동할 때 마다 1씩 거리를 증가
        # 레이저의 일렬 이동으로, 방향이 바뀔 때 마다 거리(거울의 수)가 증가함.
        while 0 <= nx < m and 0 <= ny < n:
            if a[nx][ny] == '*':
                break
            if d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                queue.append((nx, ny))
            nx += dx[i]
            ny += dy[i]

print(d[ex][ey] - 1)

"""
1. 시작점이 2개
2. 도착점이 지도의 밖으로 정해지지 않음
3. 문은 한 번 열면 계속 열린 상태 유지
"""
from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, x, y):
    n = len(a)
    m = len(a[0])
    dist = [[-1] * m for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    dist[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and a[nx][ny] != '*':
                if a[nx][ny] == '#':
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y]
                    queue.appendleft((nx, ny))
    return dist


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = ['.' + input() + '.' for _ in range(n)]
    n += 2
    m += 2
    a = ['.' * m] + a + ['.' * m]
    d0 = bfs(a, 0, 0)
    x1 = y1 = x2 = y2 = -1
    for i in range(n):
        for j in range(m):
            if a[i][j] == '$':
                if x1 == -1:
                    x1, y1 = i, j
                else:
                    x2, y2 = i, j
    d1 = bfs(a, x1, y1)
    d2 = bfs(a, x2, y2)
    ans = n * m

    for i in range(n):
        for j in range(m):
            if a[i][j] == '*':
                continue
            if d0[i][j] == -1 or d1[i][j] == -1 or d2[i][j] == -1:
                continue
            cur = d0[i][j] + d1[i][j] + d2[i][j]
            if a[i][j] == '#':
                cur -= 2
            ans = min(ans, cur)
    print(ans)

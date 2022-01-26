from collections import deque
n = int(input())
a = [[False] * (n + 1) for _ in range(n + 1)]
r1, c1, r2, c2 = map(int, input().split())
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

queue = deque()
queue.append((r1, c1, 0))
while queue:
    x, y, count = queue.popleft()
    a[x][y] = True
    if (x, y) == (r2, c2):
        print(count)
        exit()

    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not a[nx][ny]:
            queue.append((nx, ny, count + 1))
            a[nx][ny] = True

print(-1)

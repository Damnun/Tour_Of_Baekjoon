from collections import deque

n = int(input())
maps = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []

dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global maps
    count = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and maps[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
    return count
                    

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j))


print(len(result))
result.sort()
for r in result:
    print(r)

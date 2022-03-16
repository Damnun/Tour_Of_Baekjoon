import heapq
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
cost = [[float('inf')] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
cost[0][0] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = []
heapq.heappush(queue, (cost[0][0], 0, 0))
while queue:
    weight, x, y = heapq.heappop(queue)
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            if graph[nx][ny] == 0:
                cost[nx][ny] = cost[x][y] + 1
            else:
                cost[nx][ny] = cost[x][y]
            heapq.heappush(queue, (cost[nx][ny], nx, ny))
print(cost[n - 1][n - 1])

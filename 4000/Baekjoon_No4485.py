import heapq
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 1

def djikstra(count):
    cost = [[float('inf')] * n for _ in range(n)]
    cost[0][0] = graph[0][0]
    queue = []
    heapq.heappush(queue, (cost[0][0], 0, 0))
    while queue:
        weight, x, y = heapq.heappop(queue)
        if x == n - 1 and y == n - 1:
            print(f'Problem {count}: {cost[x][y]}')
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if weight + graph[nx][ny] < cost[nx][ny]:
                    cost[nx][ny] = weight + graph[nx][ny]
                    heapq.heappush(queue, (cost[nx][ny], nx, ny))


while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    djikstra(count)
    count += 1

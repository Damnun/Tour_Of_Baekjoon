from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input()))) # 맵 정보를 graph 리스트에 append

# 가능한 이동경로를 dx,dy에 저장 (좌 : 0, 우 : 1, 하 : 2, 상 : 3)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # Queue를 이용한 BFS 구현
    
    while queue: # Queue가 빌 때 까지
        x, y = queue.popleft()
        for i in range(4): # 상하좌우 4가지 경우의 수를 전부 돌림
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

print(bfs(0, 0))
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [] # 그래프 정보를 담는 리스트
data = [] # 바이러스 정보를 담는 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 바이러스가 있는 경우
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
queue = deque(data)
t_s, t_x, t_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while queue:
    virus, s, x, y = queue.popleft()
    # 정확히 s초가 지나거나 큐가 빌 때 까지 반복
    if s == t_s:
        break

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            #아직 방문하지 않았다면 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, s + 1, nx, ny))
print(graph[t_x - 1][t_y - 1])

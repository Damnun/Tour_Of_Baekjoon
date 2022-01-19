"""
NM 크기 미로, 1*1 크기의 방
빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없음
상하좌우로 이동 가능, (1, 1)에서 (N, M)이동시 벽을 부수는 최소 횟수

가중치 = 벽을 부수는 횟수
빈 방 -> 빈 방   가중치 0
빈 방 -> 벽     가중치 +1
벽 -> 벽        가중치 +1

각 칸의 값을 벽을 몇개 부수고 이동했는가로 생각
덱을 이용해서 풀이
벽을 뚫는 경우 : 가중치 1 이므로 덱의 뒤에
벽을 안 뚫는 경우 : 가중치 0 이므로 덱의 앞에

"""
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
visited[0][0] = 0

queue = deque()
queue.append((0, 0))
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == -1:
                if matrix[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft((nx, ny))
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
print(visited[n - 1][m - 1])

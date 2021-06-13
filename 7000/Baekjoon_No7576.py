from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()
m, n = map(int, input().split()) #  m : 가로, n : 세로
matrix = [list(map(int, input().split())) for _ in range(n)]


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if n > nx >= 0 and m > ny >= 0:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append([nx, ny])

# 이미 모든 토마토가 익어있는 경우
tmp = False
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            tmp = True
if not tmp:
    print("0")
    exit()

# 토마토를 익혀봅시다
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])
bfs()

# 농사 망했을 때
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            print("-1")
            exit()

# 농사 잘됐을 때
tmp = max(matrix[0])
for i in range(1, n):
        if max(matrix[i]) > tmp:
            tmp = max(matrix[i])
print(tmp - 1)

"""
BFS를 이용한 토마토 문제
원래 3층짜리 (X, Y, Z)를 이용한 토마토 문제를 풀려다가
제대로 감이 안잡혀서 1층짜리 토마토 문제를 먼저 풀어보았다.
일단 1(익은 토마토) 가 있는 곳을 queue에 삽입하여 bfs를 돌려주면
해당 1부분에서부터 bfs 순회가 이루어지고, 순회가 이루어 질때 마다 칸의 count가 1씩 더해준다
농사가 잘 됐을 경우 max에서 1을 빼주면(처음에 1로 시작하니) 원하는 day가 나오고
망했을 때는 0(안익은 토마토) 가 있는 경우이므로 이를 나누어 구분해준다.
"""
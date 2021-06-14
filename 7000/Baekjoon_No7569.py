from collections import deque

# 좌, 우, 하, 상, 아래, 위
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
queue = deque()
m, n, h = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if matrix[nx][ny][nz] == 0:
                    queue.append([nx, ny, nz])
                    matrix[nx][ny][nz] = matrix[x][y][z] + 1


# 이미 모든 토마토가 익어있는 경우
tmp = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 0:
                tmp = True
    if not tmp:
        print("0")
        exit()


# 토마토를 익혀봅시다
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 1:
                queue.append([i, j, k])
bfs()

# 흉년
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 0:
                print("-1")
                exit()

# 농사 잘 됐을때
result = 0
result = max(matrix[0][0])
for i in range(h):
    for j in range(n):
        if max(matrix[i][j]) > result:
            result = max(matrix[i][j])
print(result - 1)

"""
어제 풀었던 1차원 토마토 문제에서 진화한 3차원 토마토 문제이다
문제의 기본 틀은 변함 없지만 차원이 3차원으로 증가하여 리스트의 인덱스가 늘어나고
그에 맞게 여러 조건들을 추가해주어야 했다. 어렵진 않았는데 중간에 오타를 못봐서
시간이 오래 걸렸던 것 같다.
"""

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 이동가능경로탐색 우, 좌, 상, 하

count = 0
N = int(input())
matrix = [list(map(str, input())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]


def bfs(x, y):
    queue = [[x, y]]
    visited[x][y] = count

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if N > nx >= 0 and N > ny >= 0:
                if matrix[nx][ny] == matrix[x][y] and (not visited[nx][ny]):
                    queue.append([nx, ny])
                    visited[nx][ny] = True


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            count += 1
print(count, end=' ')

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'
visited = [[False for _ in range(N)] for _ in range(N)]

count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            count += 1
print(count)

"""
BFS를 이용한 탐색문제. 상하좌우를 돌면서 한 구역을 책정한다.
RGB의 적녹색약이 보는 시야와 일반인의 시야를 구분하는 문제인데
일단 일반인의 시야를 구한 뒤 RG를 통합하여 BFS를 다시 한번 돌려주었다.
하나 아쉬운점은 26~31 // 40~45를 함수로 축약할 수 있을 것 같다는 점인데
시간이 모자랐다.
"""

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            move_x = a + dx[i]
            move_y = b + dy[i]
            if 0 <= move_x < n and 0 <= move_y < m and data[move_x][move_y] == 1:
                data[move_x][move_y] = 0
                queue.append([move_x, move_y])


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    data = [[0]*m for _ in range(n)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        data[y][x] = 1

    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                bfs(i, j)
                data[i][j] = 0
                count += 1
    print(count)

"""
BFS를 이용한 문제
주어진 맵에서 0,0 부터 끝 까지 탐색하면서 1을 발견하면
해당 좌표를 0으로 만들고 count +1, 그 후 상하좌우로 이동가능한지 여부 확인하고
가능하다면 또 이동하면서 반복하기.
"""
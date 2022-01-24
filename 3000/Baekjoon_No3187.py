from collections import deque
r, c = map(int, input().split())
a = [list(input()) for _ in range(r)]
check = [[False] * c for _ in range(r)]
# 빈 . , 울 # , 늑 v, 양 k
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(n1, n2):
    global wolf, sheep

    check[n1][n2] = True
    queue = deque()
    queue.append((n1, n2))

    while queue:
        x, y = queue.popleft()
        if a[x][y] == 'v':
            wolf += 1
        elif a[x][y] == 'k':
            sheep += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and check[nx][ny] == False:
                if a[nx][ny] != '#':
                    queue.append((nx, ny))
                    check[nx][ny] = True


ans = [0, 0] # 양, 늑대
for i in range(r):
    for j in range(c):
        if a[i][j] != '#' and check[i][j] == False:
            sheep, wolf = 0, 0
            bfs(i, j)
            if sheep > wolf:
                ans[0] += sheep
            if wolf >= sheep:
                ans[1] += wolf

print(*ans)

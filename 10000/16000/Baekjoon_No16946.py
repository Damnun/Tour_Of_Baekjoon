from collections import deque
n, m = map(int, input().split())
check = [[False] * m for _ in range(n)]
a = [list(map(int, list(input()))) for _ in range(n)]
group = [[0] * m for _ in range(n)]
group_size = []
group_number = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(n1, n2):
    queue = deque()
    queue.append((n1, n2))
    check[n1][n2] = True
    group[n1][n2] = group_number
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 0 and not check[nx][ny]:
                    check[nx][ny] = True
                    queue.append((nx, ny))
                    group[nx][ny] = group_number
                    count += 1
    group_size.append(count)


for i in range(n):
    for j in range(m):
        if not check[i][j] and a[i][j] == 0:
            bfs(i, j)
            group_number += 1


for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(0, end='')
        else:
            near = set()
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == 0:
                        near.add(group[nx][ny])
            ans = 1
            for g in near:
                ans += group_size[g - 1]
            print(ans % 10, end='')
    print()

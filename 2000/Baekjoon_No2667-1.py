from collections import deque, Counter
from functools import reduce
import sys

input = sys.stdin.readline


def bfs(a, b, count):
    visited[a][b] = count
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = count


n = int(input())
matrix = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

count = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            count += 1
            bfs(i, j, count)

print(count)

# visited를 1차원 배열로 바꿔줌
ans = reduce(lambda x, y : x + y, visited)

# ans에서 0 이상의 값만 추려줌
ans = [x for x in ans if x > 0]

# Counter 함수를 이용해 list안의 원소들의 값을 카운트 해줌.
ans = sorted(list(Counter(ans).values()))

print('\n'.join(map(str, ans)))

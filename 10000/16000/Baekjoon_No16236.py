from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, x, y, size):
    n = len(a)
    ans = []
    d = [[-1] * n for _ in range(n)]  # 상어와 물고기의 거리
    queue = deque()
    queue.append((x, y))
    d[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1:
                ok = False
                eat = False
                if a[nx][ny] == 0:
                    ok = True
                elif a[nx][ny] < size:
                    ok = True
                    eat = True
                elif a[nx][ny] == size:
                    ok = True
                if ok:
                    queue.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
                    if eat:
                        ans.append((d[nx][ny], nx, ny))
    if not ans:
        return None
    ans.sort()
    return ans[0]


# 맵 정보를 받는 부분
# 상어의 위치를 x, y로 저장하고, 상어가 있는 곳엔 물고기가 없으므로 0을 저장
# 상어의 위치, 크기, 먹은 물고기의 수 모두 변하는 값이므로 따로 저장해주기로 함.
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            x, y = i, j
            a[i][j] = 0

ans = 0  # 상어가 먹은 물고기의 수
size = 2  # 상어의 크기
exp = 0  # 상어의 경험치 (현재 크기 수 만큼의 물고기를 섭취 시 크기가 1 증가)

while True:
    p = bfs(a, x, y, size)
    if p is None:
        break
    dist, nx, ny = p
    a[nx][ny] = 0
    ans += dist
    exp += 1

    if size == exp:
        size += 1
        exp = 0
    x, y = nx, ny

print(ans)



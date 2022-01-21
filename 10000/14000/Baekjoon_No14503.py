"""
로봇청소기 / 14503
DFS를 이용하여 풀이한 시뮬레이션 문제
"""
import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
count = 0

def go(x, y, d):
    global count
    if a[x][y] == 0:
        a[x][y] = 2
        count += 1

    # 동서남북 4방향으로 이동
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if a[nx][ny] == 0: # 다음 칸이 비어있다면 청소
            go(nx, ny, nd)
            return
        d = nd

    # 동서남북 4방향 어디로도 이동할 수 없다면
    # 뒤로 돌아간다.
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if a[nx][ny] == 1:
        return
    go(nx, ny, d) # 같은 방향에서 뒷걸음질

go(x, y, d)
print(count)


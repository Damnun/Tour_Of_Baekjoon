from collections import deque
import sys
input = sys.stdin.readline
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(int(input())):
    l = int(input())
    cur_x, cur_y = map(int, input().split())
    tar_x, tar_y = map(int, input().split())
    a = [[-1] * l for _ in range(l)]

    queue = deque()
    queue.append((cur_x, cur_y))
    a[cur_x][cur_y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < l and 0 <= ny < l:
                if a[nx][ny] == -1:
                    a[nx][ny] = a[x][y] + 1
                    queue.append((nx, ny))
    print(a[tar_x][tar_y])
    
    # 나이트의 이동 경로를 dx, dy로 만들어 준 뒤 똑같이 bfs로 count만 해주면 되는 문제였음.

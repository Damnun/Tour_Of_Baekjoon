from collections import deque
n = int(input())
matrix = [(list(map(int, input().split()))) for _ in range(n)]
queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    jump_size = matrix[x][y]
    dx = [0, jump_size]
    dy = [jump_size, 0]

    for i in range(2):
        nx = dx[i] + x
        ny = dy[i] + y

        if n <= nx or n <= ny:
            continue
        if jump_size == 0:
            continue
        if jump_size == -1:
            print("HaruHaru")
            exit(0)
        queue.append((nx, ny))

print("Hing")

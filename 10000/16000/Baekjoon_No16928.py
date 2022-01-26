from collections import deque
n, m = map(int, input().split()) # 사다리, 뱀
a = [[i] for i in range(1, 101)]
visited = [False] * 101
ladder = [[] for _ in range(101)]
snake = [[] for _ in range(101)]

for i in range(n):
    start, end = map(int, input().split())
    ladder[start].append(end)

for i in range(m):
    start, end = map(int, input().split())
    snake[start].append(end)


queue = deque()
queue.append((1, 0))

while queue:
    tmp = []
    x, count = queue.popleft()
    visited[x] = True
    if x == 100:
        print(count)
        exit()

    for i in range(1, 7):
        nx = x + i
        if 0 <= nx <= 100 and not visited[nx]:
            visited[nx] = True
            if ladder[nx]:
                queue.append((*ladder[nx], count + 1))
            if snake[nx]:
                queue.append((*snake[nx], count + 1))
            else:
                queue.append((nx, count + 1))

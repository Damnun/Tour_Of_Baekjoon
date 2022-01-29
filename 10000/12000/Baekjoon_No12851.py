from collections import deque
n, k = map(int, input().split())
visited = [0 for _ in range(100001)]

queue = deque()
queue.append((n, 0))
count, time = 0, 0

while queue:
    x, y = queue.popleft()
    visited[x] = 1
    if time != 0 and time < y:
        break
    if x == k:
        time = y
        count += 1
        visited[k] = 0
    else:
        if x - 1 >= 0 and visited[x - 1] == 0:
            queue.append([x - 1, y + 1])
        if x + 1 <= 100000 and visited[x + 1] == 0:
            queue.append([x + 1, y + 1])
        if x * 2 <= 100000 and visited[x * 2] == 0:
            queue.append([x * 2, y + 1])
print(time)
print(count)

from collections import deque

def bfs(s, t):
    queue = deque()
    queue.append((s, t, 0))
    visited = [-1] * (200)

    while queue:
        s, t, count = queue.popleft()
        if s <= t and visited[s] == -1:
            queue.append((s * 2, t + 3, count + 1))
            queue.append((s + 1, t, count + 1))
            if s == t:
                return count


c = int(input())
for i in range(c):
    s, t = map(int, input().split())
    print(bfs(s, t))

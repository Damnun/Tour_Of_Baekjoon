from collections import deque
n = int(input())
a, b = list(map(int, input().split()))
m = int(input())

result = [0 for i in range(n + 1)]
data = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)


def bfs(root):
    queue = deque()
    queue.append(root)
    visited = []

    while queue:
        n = queue.popleft()
        for i in data[n]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                result[i] = result[n] + 1


bfs(a)
if a == b:
    print("0")
else:
    print(result[b] if result[b] != 0 else -1)

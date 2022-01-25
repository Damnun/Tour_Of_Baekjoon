from collections import deque
n = int(input())
a = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    a[u - 1].append(v - 1)
    a[v - 1].append(u - 1)

b = list(map(int, input().split()))
b = [x - 1 for x in b]
order = [0] * n

for i in range(n):
    order[b[i]] = i

for i in range(n):
    a[i].sort(key=lambda x: order[x])

bfs_order = []
check = [False] * n
queue = deque()
queue.append(0)
check[0] = True

while queue:
    x = queue.popleft()
    bfs_order.append(x)
    for y in a[x]:
        if not check[y]:
            check[y] = True
            queue.append(y)

ok = True
for i in range(n):
    if bfs_order[i] != b[i]:
        ok = False
print(1 if ok else 0)

from collections import deque
f, s, g, u, d = map(int, input().split())
check = [False] * (f + 1)
dist = [0] * (f + 1)

queue = deque()
queue.append(s)
check[s] = True

while queue:
    now = queue.popleft()
    if now + u <= f and not check[now + u]:
        dist[now + u] = dist[now] + 1
        check[now + u] = True
        queue.append(now + u)
    if now - d >= 1 and not check[now - d]:
        dist[now - d] = dist[now] + 1
        check[now - d] = True
        queue.append(now - d)
if check[g]:
    print(dist[g])
else:
    print('use the stairs')

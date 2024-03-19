n = int(input())
data = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(int(input())):
    s, e = map(int, input().split())
    if e not in data[e]:
        data[s].append(e)
    if s not in data[s]:
        data[e].append(s)

queue = [1]
result = 0

while queue:
    cur = queue.pop(0)
    visited[cur] = True

    for i in data[cur]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)
            result += 1

print(result)

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [[] for _ in range(n + 1)]

for _ in range(m):
    y, x, w = map(int, input().split())
    maps[y].append((x, w))
    maps[x].append((y, w))

start, end = map(int, input().split())
_min, _max = 1, 1000000000


def bfs(t):
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    while queue:
        y = queue.popleft()
        for x, w in maps[y]:
            if x not in visited and w >= t:
                visited.add(x)
                queue.append(x)
    return True if end in visited else False


result = _min
while _min <= _max:
    mid = (_min + _max) // 2
    if bfs(mid):
        result = mid
        _min = mid + 1
    else:
        _max = mid - 1
print(result)

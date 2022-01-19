"""
LIS // d[i] = max(d[j]) + 1 // j < i // a[j] < a[i]
역추적 now, next를 통해 이전 방문을 저장해둠
from 리스트를 만들어 어디서 왔는지를 단계별로 저장
from[next] = now

재귀 사용 or 저장 해두고 역순으로 출력

"""
from collections import deque
import sys
MAX = 200000
sys.setrecursionlimit(MAX)
n, k = map(int, input().split())

visited = [False] * MAX
dist = [-1] * MAX
from_data = [-1] * MAX
visited[n] = True
dist[n] = 0

queue = deque()
queue.append(n)
while queue:
    now = queue.popleft()
    for next in [now - 1, now + 1, now * 2]:
        if next == now - 1:
            if next >= 0 and not visited[next]:
                queue.append(next)
                visited[next] = True
                dist[next] = dist[now] + 1
                from_data[next] = now
        else:
            if next < MAX and not visited[next]:
                queue.append(next)
                visited[next] = True
                dist[next] = dist[now] + 1
                from_data[next] = now

print(dist[k])

def go(n, k):
    if n != k:
        go(n, from_data[k])
    print(k, end=' ')


go(n, k)



"""
- 화면에 있는 이모티콘을 모두 복사해 클립보드에 저장 s s
- 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 > s s
- 화면에 있는 이모티콘 중 하나를 삭제 > s - 1 c
모든 연산의 시간은 1로 가정 (간선 비용이 동일 -> BFS)
S개의 이모티콘을 만드는데 걸리는 시간의 최솟값
C : 클립보드

정점 : (S, C)
"""

from collections import deque
n = int(input())
dist = [[-1] * (n + 1) for _ in range(n + 1)]

queue = deque()
queue.append((1, 0))
dist[1][0] = 0

while queue:
    s, c = queue.popleft()
    if dist[s][s] == -1:
        dist[s][s] = dist[s][c] + 1
        queue.append((s, s))

    if s + c <= n and dist[s + c][c] == -1:
        dist[s + c][c] = dist[s][c] + 1
        queue.append((s + c, c))

    if s - 1 >= 0 and dist[s - 1][c] == -1:
        dist[s - 1][c] = dist[s][c] + 1
        queue.append((s - 1, c))
ans = -1
for i in range(n + 1):
    if dist[n][i] != -1:
        if ans == -1 or ans > dist[n][i]:
            ans = dist[n][i]
print(ans)

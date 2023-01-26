import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
graph = [[] for _ in range(n + 1)]


def dfs(cur, weight):
    for i in graph[cur]:
        a, b = i
        if distance[a] == -1:
            distance[a] = weight + b
            dfs(a, weight + b)


for _ in range(n):
    cur = list(map(int, input().split()))
    cur.pop()
    a = cur.pop(0)
    while cur:
        b = cur.pop(0)
        c = cur.pop(0)
        graph[a].append([b, c])
        graph[b].append([a, c])


distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))

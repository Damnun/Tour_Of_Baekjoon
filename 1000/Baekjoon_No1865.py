import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(s):
    dis = [INF] * (n + 1)
    dis[s] = 0

    for i in range(n):
        for cur, next, cost in edges:
            if dis[next] > cost + dis[cur]:
                dis[next] = cost + dis[cur]
                if i == n - 1:
                    return True

    return False

t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    if bf(1):
        print("YES")
    else:
        print("NO")

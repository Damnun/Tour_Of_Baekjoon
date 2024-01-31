import sys
sys.setrecursionlimit(10**6)

def dfs(now, adj, visit):
    if visit[now] == 1:
        return
    else:
        visit[now] = 1
        for neighbor in adj[now]:
            dfs(neighbor, adj, visit)
    return


n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
adj_reverse = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj_reverse[b].append(a)

s, t = map(int, input().split())

fromS = [0] * (n + 1)
fromS[t] = 1
dfs(s, adj, fromS)

fromT = [0] * (n + 1)
fromT[s] = 1
dfs(t, adj, fromT)

toS = [0] * (n + 1)
dfs(s, adj_reverse, toS)

toT = [0] * (n + 1)
dfs(t, adj_reverse, toT)

count = 0
for i in range(1, n + 1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        count += 1

print(count - 2)

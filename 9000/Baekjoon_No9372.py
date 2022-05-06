import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    visited = [0] * (n + 1)
    a = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        x, y = map(int, input().split())
        a[x].append(y)
        a[y].append(x)
    
    def DFS(data, cur):
        visited[data] = 1
        for i in a[data]:
            if visited[i] == 0:
                cur = DFS(i, cur + 1)
        return cur
    
    result = DFS(1, 0)
    print(result)

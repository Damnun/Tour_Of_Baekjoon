import sys
input = sys.stdin.readline

def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]


def union(p, a, b):
    a = find(p, a)
    b = find(p, b)

    if a < b:
        p[b] = a
    elif a > b:
        p[a] = b
    else:
        return

n, m = int(input()), int(input())
p = [0] + [i for i in range(1, n + 1)]

for i in range(1, n + 1):
    graph = list(map(int, input().split()))
    for j in range(1, len(graph) + 1):
        if graph[j - 1] == 1:
            union(p, i, j)

exp = list(map(int, input().split()))
result = []
for i in exp:
    result.append(find(p, i))

if len(set(result)) == 1:
    print('YES')
else:
    print('NO')

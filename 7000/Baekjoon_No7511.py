import sys
input = sys.stdin.readline

def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]


def union(p, x, y):
    x, y = find(p, x), find(p, y)
    if x < y:
        p[y] = x
    else:
        p[x] = y


for i in range(1, int(input()) + 1):
    n = int(input())
    p = [i for i in range(n)]
    k = int(input())

    for _ in range(k):
        x, y = map(int, input().split())
        if find(p, x) != find(p, y):
            union(p, x, y)

    print(f'Scenario {i}:')
    for _ in range(int(input())):
        x, y = map(int, input().split())
        if find(p, x) != find(p, y):
            print(0)
        else:
            print(1)
    print()

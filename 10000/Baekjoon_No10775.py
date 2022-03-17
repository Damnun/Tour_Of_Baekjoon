import sys
input = sys.stdin.readline


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    a = find(a)
    b = find(b)
    p[b] = a

G = int(input())
P = int(input())
p = [i for i in range(G + 1)]
planes = [int(input()) for _ in range(P)]
answer = 0

for plane in planes:
    cur = find(plane)
    if cur == 0:
        break
    answer += 1
    union(cur - 1, cur)
print(answer)

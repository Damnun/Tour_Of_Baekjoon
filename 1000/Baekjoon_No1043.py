import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set(input().split()[1:])
party = []

for _ in range(m):
    party.append(set(input().split()[1:]))

for _ in range(m):
    for p in party:
        if p & a:
            a = a.union(p)

count = 0
for p in party:
    if p & a:
        continue
    count += 1
print(count)

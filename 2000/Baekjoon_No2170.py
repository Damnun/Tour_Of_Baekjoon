import sys
input = sys.stdin.readline

n = int(input())
lines = []
for i in range(n):
    s, e = map(int, input().split())
    lines.append((s, e))
lines.sort()

start, end = lines[0]
ans = 0

for i in range(1, n):
    cs, ce = lines[i]

    if end > cs:
        end = max(end, ce)

    else:
        ans += (end - start)
        start, end = cs, ce

ans += (end - start)
print(ans)

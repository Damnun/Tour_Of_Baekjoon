import sys
input = sys.stdin.readline

n = int(input())
x = []
y = []
s = []

for _ in range(6):
    t, cur = map(int, input().split())
    s.append([t, cur])
    if t in [1, 2]:
        x.append(cur)
    else:
        y.append(cur)

l = []
for i in range(6):
    if s[i][0] == s[(i + 2) % 6][0]:
      l.append(s[(i + 1) % 6][1])
print(((max(x) * max(y)) - (l[0] * l[1])) * n)

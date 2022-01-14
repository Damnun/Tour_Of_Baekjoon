MOD = 1000000009
data = []
t = int(input())
for i in range(t):
    data.append(int(input()))

n = max(data)
d = [1] + ([0] * n)

for i in range(1, n + 1):
    if i - 1 >= 0:
        d[i] += d[i - 1]
    if i - 2 >= 0:
        d[i] += d[i - 2]
    if i - 3 >= 0:
        d[i] += d[i - 3]
    d[i] %= MOD

for i in data:
    print(d[i])

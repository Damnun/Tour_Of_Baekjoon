limit = 10000
d = [0] * (limit + 1)
d[0] = 1

for i in range(1, limit + 1):
    if i - 1 >= 0:
        d[i] += d[i - 1]

for i in range(1, limit + 1):
    if i - 2 >= 0:
        d[i] += d[i - 2]

for i in range(1, limit + 1):
    if i - 3 >= 0:
        d[i] += d[i - 3]

for _ in range(int(input())):
    print(d[int(input())])

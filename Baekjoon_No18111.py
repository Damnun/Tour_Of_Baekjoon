n, m, b = map(int, input().split())
data = []
time = 0

for _ in range(n):
    data.append(list(map(int, input().split())))
print(set(data[0]))
def get_distance(x, y):
    return ((x ** 2) + (y ** 2)) ** 0.5


n = int(input())
data = []

for i in range(n):
    cur = list(map(int, input().split()))
    cur.append(get_distance(cur[0], cur[1]))
    data.append([i + 1, cur[3] / cur[2]])

data.sort(key=lambda x: (x[1], x[0]))

for i in data:
    print(i[0])

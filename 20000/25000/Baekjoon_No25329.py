data = {}
for _ in range(int(input())):
    time, name = input().split()
    time = int(time[0:2]) * 60 + int(time[3:])
    if name in data:
        data[name] += time
    else:
        data[name] = time

for i in data.keys():
    cost = 10
    if data[i] <= 100:
        data[i] = cost
        continue

    data[i] -= 100
    cost += (data[i] // 50) * 3
    if data[i] % 50 != 0:
        cost += 3
    data[i] = cost

for i in sorted(data.items(), key=lambda x: (-x[1], x[0])):
    print(*i)

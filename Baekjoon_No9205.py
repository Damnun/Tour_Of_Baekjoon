loop = int(input())
for _ in range(loop):
    conv_count = int(input())
    location = []

    for i in range(conv_count + 2):
        loc_x, loc_y = map(int, input().split())
        location.append((loc_x, loc_y))

    graph = [[1000] * (conv_count + 2) for _ in range(conv_count + 2)]

    # 정점 간 이동 가능 표시
    for i in range(len(location)):
        for j in range(len(location)):
            if i == j:
                graph[i][j] = 0
                continue
            x1, y1 = location[i]
            x2, y2 = location[j]
            distance = abs(x1 - x2) + abs(y1 - y2)
            if distance <= 1000:
                graph[i][j] = 1

    for i in range(len(location)):
        for j in range(len(location)):
            for k in range(len(location)):
                if graph[j][i] + graph[i][k] < graph[j][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]

    if 0 < graph[0][conv_count + 1] < max:
        print("happy")
    else:
        print("sad")

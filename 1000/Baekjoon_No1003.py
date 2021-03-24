for _ in range(int(input())):
    data = int(input())
    result = [[1, 0], [0, 1], [1, 1]]

    if data >= 2:
        for i in range(2, data):
            result.append([result[i][1], result[i][0] + result[i][1]])

    print(result[data][0], result[data][1])

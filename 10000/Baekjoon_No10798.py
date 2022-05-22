a = [[0] * 15 for i in range(5)]

for i in range(5):
    data = list(input())
    for j in range(len(data)):
        a[i][j] = data[j]

for i in range(15):
    for j in range(5):
        if a[j][i] == 0:
            continue;
        else:
            print(a[j][i], end='')
